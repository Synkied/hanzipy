# coding:utf-8
import csv
import json
import logging
import re
from pathlib import Path
from anytree import Node, RenderTree

from hanzipy.exceptions import NotAHanziCharacter

logging.basicConfig(level=logging.DEBUG)


RADICAL_REGEX = r"[一丨丶⺀丿乙⺃乚⺄亅丷]"
CURRENT_DIR = BASE_DIR = Path(__file__).parent


# Adds an item to a list if it does not already exist
def append_if_not_exists(list_items, new_item):
    if new_item not in list_items:
        list_items.append(new_item)


# Adds an item to a list if it does not already exist
def extend_if_not_exists(list_items, new_list_items):
    for item in new_list_items:
        append_if_not_exists(list_items, item)


def remove_duplicates(list_items, charater):
    item_set = set(list_items)
    if charater in item_set:
        item_set.remove(charater)
    return list(item_set)


# Traverses from the tree root and outputs the tree string representation
def build_tree_string(root, character):
    string = ""
    for pre, fill, node in RenderTree(root):
        string += "%s%s" % (pre, node.name) + "\n"
    string = string.strip()

    return "" if string == character else string


class HanziDecomposer:
    def __init__(self):
        self.characters = {}
        self.radicals = {}
        self.characters_with_component = {}
        self.noglyph = "No glyph available"
        self.init_decomposition()
        self.compile_all_components()

    def init_decomposition(
        self,
    ):
        # Reading in cjk_decomp - Decomposition Database
        decomp_filepath = "{}/data/cjk_decomp.txt".format(CURRENT_DIR)
        with open(decomp_filepath, encoding="utf-8") as decomp_file:
            lines = decomp_file.readlines()

            for line in lines:
                colonsplit = line.split(":")
                character = colonsplit[0]
                decomposition = colonsplit[1]
                openbracket = decomposition.index("(")
                closebracket = decomposition.index(")")
                decomposition_type = decomposition[0:openbracket]
                components = decomposition[openbracket + 1 : closebracket].split(
                    ","
                )  # noqa
                self.characters[character] = {
                    "decomposition_type": decomposition_type,
                    "components": components,
                }

        # Reading in radical list
        radical_filepath = "{}/data/radical_with_meanings.json".format(CURRENT_DIR)
        with open(radical_filepath, encoding="utf-8") as radicals_file:
            self.radicals = json.load(radicals_file)

    def compile_all_components(
        self,
    ):
        filepath = "{}/data/chinese_charfreq_simpl_trad.csv".format(CURRENT_DIR)
        with open(filepath, encoding="utf-8") as freq_file:
            csvreader = csv.reader(freq_file)
            next(csvreader, None)  # skip the headers

            for row in csvreader:
                character = row[1]
                line_num = row[0]
                decomposition = self.decompose(character)

                for component in decomposition["once"]:
                    if component not in self.characters_with_component:
                        if component != self.noglyph:
                            self.characters_with_component.setdefault(component, [])
                            self.characters_with_component[component].append(character)

                    elif component != self.noglyph:
                        self.characters_with_component[component].append(character)

                for component in decomposition["radical"]:
                    if component not in self.characters_with_component:
                        if component != self.noglyph and not re.search(
                            RADICAL_REGEX, component
                        ):
                            self.characters_with_component.setdefault(
                                component,
                                [],
                            )
                            if self.is_unique(
                                self.characters_with_component[component],
                                character,
                            ):  # noqa
                                self.characters_with_component[component].append(
                                    character
                                )  # noqa

                        elif component != self.noglyph and not re.search(
                            RADICAL_REGEX, component
                        ):
                            if self.is_unique(
                                self.characters_with_component[component],
                                character,
                            ):  # noqa
                                self.characters_with_component[component].append(
                                    character
                                )  # noqa

        logging.info("Done compiling {} characters".format(int(line_num) - 1))
        return self.characters_with_component

    def is_unique(self, array_list, token):
        unique = True

        for item in array_list:
            if item == token:
                unique = False

        return unique

    def decompose_many(self, characterstring, decomposition_type=None):
        characterstring = str(characterstring)
        # Not Hanzi
        if not re.search("[\u4e00-\u9fff]", characterstring):
            raise NotAHanziCharacter(characterstring)

        decomposed_components = {}

        # remove spaces from input string
        characterstring = characterstring.replace(r"/\s/g", "")
        if not characterstring:
            raise "Invalid input"

        for idx, char in enumerate(characterstring):
            one_character = characterstring[idx : idx + 1]

            # don't decompose the same character more than once
            if one_character in decomposed_components.keys():
                continue

            decomposed_components[one_character] = self.decompose(
                one_character, decomposition_type
            )

        return decomposed_components

    # Builds a tree reprentation of the radical decomposition of `character`
    def tree(self, character):
        character = character.replace(r"/\s/g", "")
        if self.is_messy(character):
            logging.error(self.is_messy(character))
            return "Invalid Input"

        decomposed_char = {}
        tree = Node(character)
        # tree.create_node(identifier = character, tag = character)

        decomposed_char = {
            "character": character,
            "components": self.tree_radical_up_decomposition(character, tree),
            "tree": build_tree_string(tree, character),
        }

        string = json.dumps(decomposed_char)
        jsonoutput = json.loads(string)

        return jsonoutput

    def decompose(self, character, decomposition_type=None):
        """
        Type of decomp:
        1 = Only 2 components，
        2 = Radical,
        3 = Graphical,
        4 = Radical and up
        """
        character = character.replace(r"/\s/g", "")
        if self.is_messy(character):
            logging.error(self.is_messy(character))
            return "Invalid Input"

        decomposed_char = {}

        if not decomposition_type:
            decomposed_char = {
                "character": character,
                "once": self.once_decomposition(character),
                "radical": self.radical_decomposition(character),
                "graphical": self.graphical_decomposition(character),
                "radical_up": self.radical_up_decomposition(character),
            }

        elif decomposition_type == 1:
            decomposed_char = {
                "character": character,
                "components": self.once_decomposition(character),
            }
        elif decomposition_type == 2:
            decomposed_char = {
                "character": character,
                "components": self.radical_decomposition(character),
            }
        elif decomposition_type == 3:
            decomposed_char = {
                "character": character,
                "components": self.graphical_decomposition(character),
            }
        elif decomposition_type == 4:
            decomposed_char = {
                "character": character,
                "components": self.radical_up_decomposition(character),
            }
        else:
            return

        string = json.dumps(decomposed_char)
        jsonoutput = json.loads(string)

        return jsonoutput

    # Functions to help with Decomposition
    def once_decomposition(self, character):
        components = self.get_components(character)
        return self.replace_numbers(components)

    # Builds a tree representation and decomposes the character until reaching radicals, but including the components above too
    def tree_radical_up_decomposition(self, character, tree):
        final_array = []
        if self.is_radical(character):
            append_if_not_exists(final_array, character)
        else:
            components = self.get_components(character)

            append_if_not_exists(final_array, character)  # Additional

            if len(components) == 2:
                for child in components:
                    extend_if_not_exists(final_array, self.tree_radical_up_decomposition(child, Node(child, parent=tree)))  # fmt: skip
            else:
                append_if_not_exists(final_array, character)

        return self.replace_numbers(final_array)

    # Decomposes the character until reaching radicals, but including the containing components too
    def radical_up_decomposition(self, character):
        final_array = []
        if self.is_radical(character):
            append_if_not_exists(final_array, character)
            # final_array.append(character)
        else:
            components = self.get_components(character)

            final_array.append(character)  # Also add the containing components
            if len(components) == 2:
                for j in range(2):
                    extend_if_not_exists(final_array, self.radical_up_decomposition(components[j]))  # fmt: skip
                    # final_array.extend(self.radical_up_decomposition(components[j]))
            else:
                append_if_not_exists(final_array, character)
                # final_array.append(character)

        return self.replace_numbers(final_array)

    def radical_decomposition(self, character):
        final_array = []
        if self.is_radical(character):
            append_if_not_exists(final_array, character)
            # final_array.append(character)
        else:
            components = self.get_components(character)

            if len(components) == 2:
                for j in range(2):
                    extend_if_not_exists(final_array, self.radical_decomposition(components[j]))  # fmt: skip
                    # final_array.extend(self.radical_decomposition(components[j]))
            else:
                append_if_not_exists(final_array, character)
                # final_array.append(character)

        return self.replace_numbers(final_array)

    def graphical_decomposition(self, character):
        final_array = []

        components = self.get_components(character)
        if len(components) == 2:
            for j in range(2):
                extend_if_not_exists(final_array, self.graphical_decomposition(components[j]))  # fmt: skip
                # final_array.extend(self.graphical_decomposition(components[j]))
        else:
            if not character.isdigit():
                append_if_not_exists(final_array, character)
                # final_array.append(character)
            else:
                extend_if_not_exists(final_array, self.resolve_number(character))
                # final_array.extend(self.resolve_number(character))

        return final_array

    def replace_numbers(self, characters):
        finalreview = []

        for char in characters:
            if not char.isdigit():
                finalreview.append(char)

            else:
                # finalreview.append("No glyph available")
                finalreview.append(char)

        return finalreview

    def resolve_number(self, number):
        numbers_cleared = []
        components = self.get_components(number)

        for component in components:
            if not component.isdigit():
                numbers_cleared.append(component)
            else:
                numbers_cleared.extend(self.resolve_number(component))

        return numbers_cleared

    def get_characters_with_component(self, component):
        if component in self.radicals.keys():
            components = self.find_same_meaning_radicals(component)
            characters = []

            for component in components:
                if self.characters_with_component[component]:
                    characters.extend(self.characters_with_component[component])

            return characters
        else:
            if component in self.characters_with_component.keys():
                return self.characters_with_component[component]

            return

    def find_same_meaning_radicals(self, radical):
        same_radicals = []
        meaning = self.radicals[radical]

        for radical in self.radicals:
            if radical in self.radicals:
                if self.radicals[radical] == meaning:
                    same_radicals.append(radical)

        return same_radicals

    def is_radical(self, character):
        is_rad = False

        if self.radicals.get(character):
            is_rad = True

        return is_rad

    def get_components(self, character):
        if self.component_exists(character):
            if self.characters[character]["decomposition_type"] == "c":
                return character
            else:
                return self.characters[character]["components"]

        else:
            return character

    def get_radical_meaning(self, radical):
        if self.is_radical(radical):
            return self.radicals[radical]
        else:
            return

    def component_exists(self, component):
        return component in self.characters

    def is_messy(self, character):
        # If no input is sent
        if not character:
            return True

        # If it's not a Chinese character
        return not self.get_components(character)


if __name__ == "__main__":
    logging.info("Compiling Hanzi characters data...")

    # Compile Components into an object array for easy lookup
    hanzi = HanziDecomposer()

    res = hanzi.decompose("是")
    print(res)
