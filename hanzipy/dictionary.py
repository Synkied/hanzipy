import logging
import re
from math import sqrt
from pathlib import Path

from hanzipy.decomposer import HanziDecomposer
from hanzipy.exceptions import NotAHanziCharacter

logging.basicConfig(level=logging.DEBUG)

CURRENT_DIR = BASE_DIR = Path(__file__).parent
CCEDICT_STARTING_LINE = 30


class PinyinSyllable:
    def __init__(self, raw_syllable):
        self.raw_syllable = raw_syllable

    def syllable(self):
        return self.raw_syllable[: len(self.raw_syllable) - 1]

    def initial(self):
        initial = ""
        if self.raw_syllable[1:2] == "h":
            # Take into zh, ch, sh
            initial = self.raw_syllable[0:2]
        else:
            initial = self.raw_syllable[0:1]

        return initial

    def final(self):
        syllable = self.syllable()
        rhyme = syllable.replace(self.initial(), "")
        return rhyme


class HanziDictionary:
    def __init__(self):
        self.dictionary_simplified = {}
        self.dictionary_traditional = {}
        self.irregular_phonetics = {}
        self.char_freq = {}
        self.character_frequency_count_index = []
        self.word_freq = {}
        self.last_search_query = ""
        self.compute_dictionary()

    def compute_dictionary(self):
        logging.debug("Compiling hanzi characters dictionary...")

        ccedict_filepath = "{}/data/cedict_ts.u8".format(CURRENT_DIR)

        with open(ccedict_filepath) as ccedict_file:
            lines = ccedict_file.readlines()
            self.load_frequency_data()

            def next_traditional_char(idx):
                if idx < len(lines):
                    nextcharacter = lines[idx].split(" ")
                    nextcheck = nextcharacter[0]
                    return nextcheck

                return ""

            def next_simplified_char(idx):
                if idx < len(lines):
                    nextcharacter = lines[idx].split(" ")
                    nextcheck = nextcharacter[1]
                    return nextcheck

                return ""

            def get_elements(line):
                openbracket = line.index("[")
                closebracket = line.index("]")
                defStart = line.index("/")
                defClose = line.rindex("/")
                pinyin = line[openbracket + 1 : closebracket]
                definition = line[defStart + 1 : defClose]
                elements = line.split(" ")
                traditional = elements[0]
                simplified = elements[1]

                element = {
                    "traditional": traditional,
                    "simplified": simplified,
                    "pinyin": pinyin,
                    "definition": definition,
                }

                return element

            for idx, line in enumerate(lines[CCEDICT_STARTING_LINE:]):
                hanzi_dict = [get_elements(line)]

                while hanzi_dict[0]["traditional"] == next_traditional_char(
                    idx + 1
                ) and hanzi_dict[0]["simplified"] == next_simplified_char(idx + 1):
                    hanzi_dict.append(get_elements(idx + 1))
                    idx += 1

                simplified = self.dictionary_simplified.get(hanzi_dict[0]["simplified"])
                traditional = self.dictionary_traditional.get(
                    hanzi_dict[0]["traditional"]
                )

                if simplified:
                    newhanzi_dict = simplified
                    for element in hanzi_dict:
                        newhanzi_dict.append(element)

                    self.dictionary_simplified[
                        hanzi_dict[0]["simplified"]
                    ] = newhanzi_dict
                elif traditional:
                    newhanzi_dict = traditional

                    for element in hanzi_dict:
                        newhanzi_dict.append(element)

                    self.dictionary_traditional[
                        hanzi_dict[0]["traditional"]
                    ] = newhanzi_dict
                else:
                    self.dictionary_simplified[hanzi_dict[0]["simplified"]] = hanzi_dict
                    self.dictionary_traditional[
                        hanzi_dict[0]["traditional"]
                    ] = hanzi_dict

    def definition_lookup(self, word, script_type=None):
        # Not Hanzi
        if not re.search("[\u4e00-\u9fff]", word):
            raise NotAHanziCharacter(word)

        try:
            if not script_type:
                if self.determine_if_simplfied_char(word):
                    return self.dictionary_simplified[word]

                if not self.determine_if_simplfied_char(word):
                    return self.dictionary_traditional[word]

            else:
                if script_type == "simplified":
                    return self.dictionary_simplified[word]
                elif script_type == "traditional":
                    return self.dictionary_traditional[word]
        except KeyError:
            raise KeyError(f"{word} not available in {script_type} dictionary.")

    def dictionary_search(self, character, character_type=None):
        """Types: Only = Just the characters and no alternatives.
        If not then finds all cases of that character
        """

        search_result = []
        regexstring = "^("

        if character_type == "only":
            for idx, char in enumerate(character):
                if idx < len(character) - 1:
                    regexstring = regexstring + character[idx : idx + 1] + "|"
                else:
                    regexstring = regexstring + character[idx : idx + 1] + ")+$"

        else:
            regexstring = "[" + character + "]"

        # First check for simplified.
        for word in self.dictionary_simplified:
            if self.dictionary_simplified.get(word):
                if re.search(regexstring, word):
                    search_result.extend(self.dictionary_simplified[word])

        # If there's nothing to be found,
        # then try and look for traditional entries.
        if len(search_result) == 0:
            for word in self.dictionary_traditional:
                if self.dictionary_simplified.get(word):
                    if re.search(regexstring, word):
                        search_result.extend(self.dictionary_traditional[word])

        return search_result

    def get_examples(self, character):
        """Does a dictionary search and finds the most useful example words"""

        potiental_examples = self.dictionary_search(character)
        all_frequencies = []
        search_result = {
            "high_frequency": [],
            "mid_frequency": [],
            "low_frequency": [],
        }

        for potential_example in potiental_examples:
            # Create Array of Frequency Points to calculate distributions
            # It takes the frequency accounts of both scripts into account.

            word_simplified = potential_example["simplified"]
            word_traditional = potential_example["traditional"]

            total_frequency = 0

            if self.word_freq.get(word_simplified):
                total_frequency += int(self.word_freq[word_simplified])

            if self.word_freq.get(word_traditional):
                total_frequency += int(self.word_freq[word_traditional])

            all_frequencies.append(total_frequency)

        # Calculate mean, variance + sd
        all_frequencies.sort(reverse=True)

        def compute_mean():
            total = 0

            for freq in all_frequencies:
                total += int(freq)

            mean = total / len(all_frequencies)
            return mean

        def compute_variance():
            total = 0

            for freq in all_frequencies:
                temp = int(freq) - mean
                total += temp * temp

            variance = total / len(all_frequencies)
            return variance

        mean = compute_mean()
        variance = compute_variance()
        sd = sqrt(variance)

        # Create frequency categories
        def determine_freq_categories():
            def append_frequency(word):
                simplified_char_freq = self.word_freq.get(word["simplified"])

                if simplified_char_freq:
                    simplified_char_freq = int(simplified_char_freq)
                    if simplified_char_freq < low_range:
                        search_result["low_frequency"].append(word)

                    if (
                        simplified_char_freq >= mid_range[1]
                        and simplified_char_freq < mid_range[0]
                    ):
                        search_result["mid_frequency"].append(word)

                    if simplified_char_freq >= high_range:
                        search_result["high_frequency"].append(word)

            if mean - sd < 0:
                low_range = 0 + mean / 3
            else:
                low_range = mean - sd

            mid_range = [mean + sd, low_range]
            high_range = mean + sd

            for potential_example in potiental_examples:
                word = potential_example

                if self.word_freq.get(word["simplified"]):
                    append_frequency(word)

        determine_freq_categories()

        return search_result

    def determine_if_simplfied_char(self, character):
        if character in self.dictionary_simplified.keys():
            return True

        if character in self.dictionary_traditional.keys():
            return False

    def load_frequency_data(self):
        logging.debug("Starting to read frequency data")

        leiden_freq = "{}/data/leiden_freq_data.txt".format(CURRENT_DIR)
        leiden_freq_no_variants = "{}/data/leiden_freq_variants_removed.txt".format(
            CURRENT_DIR
        )  # noqa

        with open(leiden_freq) as leiden_freq_file:
            lines = leiden_freq_file.readlines()

            for line in lines:
                line = line.rstrip("\r\n")
                splits = line.split(",")
                word = splits[0]
                freq = splits[1]
                self.word_freq[word] = freq

        with open(leiden_freq_no_variants) as leiden_freq_no_variants_file:
            lines = leiden_freq_no_variants_file.readlines()

            for line in lines:
                line = line.rstrip("\r\n")
                splits = line.split("\t")
                number = int(splits[0])
                character = splits[1]

                self.char_freq[character] = {
                    "number": number,
                    "character": character,
                    "count": splits[2],
                    "percentage": splits[3],
                    "pinyin": splits[4],
                    "meaning": splits[5],
                }

                self.character_frequency_count_index.insert(number, character)

            logging.debug("Frequency data loaded")

    def load_irregular_phonetics(self):
        irregular_phonetics = "{}/data/irregular_phonetics.txt".format(CURRENT_DIR)

        with open(irregular_phonetics) as irregular_phonetics_file:
            lines = irregular_phonetics_file.readlines()
            for line in lines:
                line = line.rstrip("\r\n")
                splits = line.split(":")
                character = splits[0]
                pinyin = splits[1]
                self.irregular_phonetics[character] = pinyin

    def get_pinyin(self, character):
        # These are for components not found in CC-CEDICT.
        if character in self.dictionary_simplified.keys():
            pinyinarray = []

            for char in self.dictionary_simplified[character]:
                pinyinarray.append(char["pinyin"])

            return pinyinarray

        if character in self.dictionary_traditional.keys():
            pinyinarray = []

            for char in self.dictionary_traditional[character]:
                pinyinarray.append(char["pinyin"])

            return pinyinarray

        if character in self.irregular_phonetics.keys():
            return [self.irregular_phonetics[character]]

        if not re.search(
            character, r"/[㇐㇇㇚𤴓𠂇㇒㇑⺊阝㇟⺀㇓㇝𪜋⺁𠮛㇔龶㇃丆㇏⺌⺹⺆㇛㇠㇆⺧⺮龸⺈㇗龴㇕㇈㇖⺤㇎⺺䧹㇂㇉⺪㇀]"
        ):  # noqa
            return

        if not isinstance(character, int):
            return

        return

    def determine_phonetic_regularity(self, decomposition):
        regularities = {}
        phonetic_pinyin = []

        # An object is not passed to this function,
        # create the decomposition object with the character inp:
        if not isinstance(decomposition, dict):
            decomposition = HanziDecomposer().decompose(decomposition)

        # Get all possible pronunciations for character
        charpinyin = self.get_pinyin(decomposition["character"])
        if not charpinyin:
            return

        # Determine phonetic regularity for components on level 1 decomposition
        for component in decomposition["once"]:
            # Get the pinyin of the component
            phonetic_pinyin = self.get_pinyin(component)

            for pinyin in charpinyin:
                # Compare it with all the possible pronunciations
                # of the character

                # If the object store has no character pinyin stored yet,
                # create the point
                regularities.setdefault(
                    pinyin,
                    {
                        "character": decomposition["character"],
                        "component": [],
                        "phonetic_pinyin": [],
                        "regularity": [],
                    },
                )

                if not phonetic_pinyin:
                    # If the component has no pronunciation found,
                    # nullify the regularity computation
                    regularities[pinyin]["phonetic_pinyin"].append(None)
                    regularities[pinyin]["component"].append(component)
                    regularities[pinyin]["regularity"].append(None)
                else:
                    # Compare the character pinyin
                    # to all possible phonetic pinyin pronunciations
                    for phon_pinyin in phonetic_pinyin:
                        regularities[pinyin]["phonetic_pinyin"].append(phon_pinyin)
                        regularities[pinyin]["component"].append(component)
                        regularities[pinyin]["regularity"].append(
                            self.get_regularity_scale(pinyin, phon_pinyin)
                        )

        for component in decomposition["radical"]:
            # Get the pinyin of the component
            phonetic_pinyin = self.get_pinyin(component)

            for pinyin in charpinyin:
                # Compare it with all the possible pronunciations
                # of the character
                # Init Object
                regularities.setdefault(
                    pinyin,
                    {
                        "character": decomposition["character"],
                        "component": [],
                        "phonetic_pinyin": [],
                        "regularity": [],
                    },
                )

                if not phonetic_pinyin:
                    # If the component has no pronunciation found,
                    # nullify the regularity computation
                    regularities[pinyin]["phonetic_pinyin"].append(None)
                    regularities[pinyin]["component"].append(component)
                    regularities[pinyin]["regularity"].append(None)
                else:
                    # Compare the character pinyin to
                    # all possible phonetic pinyin pronunciations
                    for phon_pinyin in phonetic_pinyin:
                        regularities[pinyin]["phonetic_pinyin"].append(phon_pinyin)
                        regularities[pinyin]["component"].append(component)
                        regularities[pinyin]["regularity"].append(
                            self.get_regularity_scale(pinyin, phon_pinyin)
                        )

        return regularities

    def get_character_frequency(self, character):
        # Not Hanzi
        if not re.search("[\u4e00-\u9fff]", character):
            raise NotAHanziCharacter(character)

        dict_entry = self.definition_lookup(character)

        # Check if this character has a lookup
        if dict_entry and dict_entry[0]:
            # Check if we can return a simplified version
            if self.char_freq[dict_entry[0]["simplified"]]:
                return self.char_freq[dict_entry[0]["simplified"]]

            else:
                # If not, then this is could be a traditional character
                # that possibly exists in the frequency list
                if self.char_freq[character]:
                    return self.char_freq[character]
                else:
                    # If not, this is a very uncommon character
                    raise "Character not found"

            return self.char_freq[character]

        elif self.char_freq[character]:
            # In the unlikely case that we don't have a dictionary entry
            # but it exists in the frequency list
            return self.char_freq[character]
        else:
            raise "Character not found"

    def get_character_in_frequency_list_by_position(self, position):
        return self.get_character_frequency(
            self.character_frequency_count_index[position - 1]
        )

    # Helper Functions
    def get_regularity_scale(self, charpinyin, phonetic_pinyin):
        if not charpinyin or not phonetic_pinyin:
            return

        regularity = 0
        charpinyin = PinyinSyllable(charpinyin.lower())
        phonetic_pinyin = PinyinSyllable(phonetic_pinyin.lower())

        # Regularity Scale:
        # 0 = No regularity
        # 1 = Exact Match (with tone)
        # 2 = Syllable Match (without tone)
        # 3 = Similar in Initial
        # 4 = Similar in Final

        # First test for Scale 1 & 2
        if charpinyin.syllable() == phonetic_pinyin.syllable():
            regularity = 2
            if charpinyin.raw_syllable == phonetic_pinyin.raw_syllable:
                regularity = 1

        # If still no regularity found,
        # test for initial & final regularity (scale 3 & 4)
        if regularity == 0:
            if charpinyin.final() == phonetic_pinyin.final():
                regularity = 4
            else:
                if charpinyin.initial() == phonetic_pinyin.initial():
                    regularity = 3

        return regularity


if __name__ == "__main__":
    logging.info("Compiling Hanzi characters dictionary...")

    # Compile Components into an object array for easy lookup
    hanzi_dict = HanziDictionary()
