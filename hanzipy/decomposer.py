# coding:utf-8
import csv
import json
import logging
import re
from pathlib import Path

from hanzipy.exceptions import NotAHanziCharacter

logging.basicConfig(level=logging.DEBUG)


RADICAL_REGEX = r"[一丨丶⺀丿乙⺃乚⺄亅丷]"
CURRENT_DIR = BASE_DIR = Path(__file__).parent


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
        with open(decomp_filepath) as decomp_file:
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
        with open(radical_filepath) as radicals_file:
            self.radicals = json.load(radicals_file)

    def compile_all_components(
        self,
    ):
        filepath = "{}/data/chinese_charfreq_simpl_trad.csv".format(CURRENT_DIR)
        with open(filepath) as freq_file:
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
        if not re.search(u"[\u4e00-\u9fff]", characterstring):
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

    def decompose(self, character, decomposition_type=None):
        """
        Type of decomp:
        1 = Only 2 components，
        2 = Radical,
        3 = Graphical
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

        else:
            return

        string = json.dumps(decomposed_char)
        jsonoutput = json.loads(string)

        return jsonoutput

    # Functions to help with Decomposition
    def once_decomposition(self, character):
        components = self.get_components(character)
        return self.replace_numbers(components)

    def radical_decomposition(self, character):
        final_array = []
        if self.is_radical(character):
            final_array.append(character)
        else:
            components = self.get_components(character)

            if len(components) == 2:
                for j in range(2):
                    final_array.extend(self.radical_decomposition(components[j]))
            else:
                final_array.append(character)

        return self.replace_numbers(final_array)

    def graphical_decomposition(self, character):
        final_array = []

        components = self.get_components(character)
        if len(components) == 2:
            for j in range(2):
                final_array.extend(self.graphical_decomposition(components[j]))

        else:
            if not character.isdigit():
                final_array.append(character)
            else:
                final_array.extend(self.resolve_number(character))

        return final_array

    def replace_numbers(self, characters):
        finalreview = []

        for char in characters:
            if not char.isdigit():
                finalreview.append(char)

            else:
                finalreview.append("No glyph available")

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
