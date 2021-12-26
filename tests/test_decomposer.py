# coding:utf-8
import json
from pathlib import Path

from hanzipy.decomposer import HanziDecomposer
from hanzipy.exceptions import NotAHanziCharacter

import pytest

CURRENT_DIR = BASE_DIR = Path(__file__).parent.parent


@pytest.fixture
def hanzi_decomposer():
    return HanziDecomposer()


class TestDecomposer:
    def test_decompose(self, hanzi_decomposer):
        decomposition_keys = ["character", "once", "radical", "graphical"]
        result = hanzi_decomposer.decompose("是")

        assert list(result.keys()) == decomposition_keys
        assert result == {
            "character": "是",
            "once": ["日", "𤴓"],
            "radical": ["日", "一", "龰"],
            "graphical": ["口", "一", "一", "龰"],
        }

        result = hanzi_decomposer.decompose("爱")

        assert list(result.keys()) == decomposition_keys
        print(result)
        assert result == {
            "character": "爱",
            "once": ["No glyph available", "友"],
            "radical": ["爫", "冖", "𠂇", "又"],
            "graphical": ["爫", "冖", "𠂇", "㇇", "㇏"],
        }

    def test_decompose_decomposition_type(self, hanzi_decomposer):
        decomposition_keys = ["character", "components"]
        result = hanzi_decomposer.decompose("是", 1)

        assert list(result.keys()) == decomposition_keys
        assert result == {
            "character": "是",
            "components": ["日", "𤴓"],
        }

    def test_decompose_many(self, hanzi_decomposer):
        phrase = "是的"
        result = hanzi_decomposer.decompose_many(phrase)

        assert list(result.keys()) == [char for char in phrase]
        assert result == {
            "是": {
                "character": "是",
                "graphical": ["口", "一", "一", "龰"],
                "once": ["日", "𤴓"],
                "radical": ["日", "一", "龰"],
            },
            "的": {
                "character": "的",
                "graphical": ["口", "一", "㇒", "㇆", "㇒", "丶"],
                "once": ["白", "勺"],
                "radical": ["白", "勹", "丶"],
            },
        }

        phrase = "平仮名"
        result = hanzi_decomposer.decompose_many(phrase)

        assert list(result.keys()) == [char for char in phrase]
        assert result == {
            "平": {
                "character": "平",
                "once": ["干", "丷"],
                "radical": ["干", "丷"],
                "graphical": ["一", "一", "丨", "丷"],
            },
            "仮": {
                "character": "仮",
                "once": ["亻", "反"],
                "radical": ["亻", "⺁", "又"],
                "graphical": ["㇒", "丨", "丿", "㇒", "㇇", "㇏"],
            },
            "名": {
                "character": "名",
                "once": ["夕", "口"],
                "radical": ["夕", "口"],
                "graphical": ["夕", "口"],
            },
        }

        with pytest.raises(NotAHanziCharacter):
            phrase = "test phrase"
            hanzi_decomposer.decompose_many(phrase)

        with pytest.raises(NotAHanziCharacter):
            phrase = "한글"
            hanzi_decomposer.decompose_many(phrase)

        with pytest.raises(NotAHanziCharacter):
            phrase = "ひらがな"
            hanzi_decomposer.decompose_many(phrase)

    def test_is_radical(self, hanzi_decomposer):
        result = hanzi_decomposer.is_radical("是")
        assert result is False

        result = hanzi_decomposer.is_radical("一")
        assert result is True

        result = hanzi_decomposer.is_radical("test")
        assert result is False

    def test_all_radicals(self, hanzi_decomposer):
        radical_filepath = "{}/data/radical_with_meanings.json".format(CURRENT_DIR)
        with open(radical_filepath) as radicals_file:
            radicals = json.load(radicals_file)
            for radical in radicals.keys():
                assert hanzi_decomposer.is_radical(radical) is True

    def test_get_radical_meaning(self, hanzi_decomposer):
        # valid component and results
        result = hanzi_decomposer.get_radical_meaning("一")
        assert result == "one"

        # no result
        result = hanzi_decomposer.get_radical_meaning("test")
        assert result is None

    def test_get_characters_with_component(self, hanzi_decomposer):
        # valid component and results
        result = hanzi_decomposer.get_characters_with_component("囗")
        assert result == [
            "国",
            "因",
            "西",
            "回",
            "四",
            "口",
            "团",
            "图",
            "围",
            "固",
            "困",
            "园",
            "圆",
            "圈",
            "囚",
            "圃",
            "圜",
            "囿",
            "圉",
            "囤",
            "圄",
            "囹",
            "囡",
            "囫",
            "囵",
            "囝",
            "圊",
            "釦",
        ]

        # no result
        result = hanzi_decomposer.get_characters_with_component("test")
        assert result is None

    def test_component_exists(self, hanzi_decomposer):
        result = hanzi_decomposer.component_exists("乂")
        assert result is True

        result = hanzi_decomposer.component_exists("toto")
        assert result is False
