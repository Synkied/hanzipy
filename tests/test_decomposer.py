# coding:utf-8
import json
from pathlib import Path

from hanzipy.decomposer import HanziDecomposer

import pytest

CURRENT_DIR = BASE_DIR = Path(__file__).parent.parent


@pytest.fixture
def hanzi_decomposer():
    return HanziDecomposer()


class TestDecomposer:
    def test_decompose(self, hanzi_decomposer):
        decomposition_keys = ['character', 'once', 'radical', 'graphical']
        result = hanzi_decomposer.decompose('是')

        assert list(result.keys()) == decomposition_keys
        assert result == {
            'character': '是',
            'once': ['日', '𤴓'],
            'radical': ['日', '一', '龰'],
            'graphical': ['口', '一', '一', '龰']
        }

    def test_decompose_decomposition_type(self, hanzi_decomposer):
        decomposition_keys = ['character', 'components']
        result = hanzi_decomposer.decompose('是', 1)

        assert list(result.keys()) == decomposition_keys
        assert result == {
            'character': '是',
            'components': ['日', '𤴓'],
        }

    def test_decompose_many(self, hanzi_decomposer):
        phrase = '是的'
        result = hanzi_decomposer.decompose_many(phrase)

        assert list(result.keys()) == [char for char in phrase]
        assert result == {
            '是': {
                'character': '是',
                'graphical': ['口', '一', '一', '龰'],
                'once': ['日', '𤴓'],
                'radical': ['日', '一', '龰']
            },
            '的': {
                'character': '的',
                'graphical': ['口', '一', '㇒', '㇆', '㇒', '丶'],
                'once': ['白', '勺'],
                'radical': ['白', '勹', '丶']
            }
        }

    def test_is_radical(self, hanzi_decomposer):
        result = hanzi_decomposer.is_radical('是')
        assert result is False

        result = hanzi_decomposer.is_radical('一')
        assert result is True

    def test_all_radicals(self, hanzi_decomposer):
        radical_filepath = '{}/data/radical_with_meanings.json'.format(
            CURRENT_DIR)
        with open(radical_filepath) as radicals_file:
            radicals = json.load(radicals_file)
            for radical in radicals.keys():
                assert hanzi_decomposer.is_radical(radical) is True

    def test_get_radical_meaning(self, hanzi_decomposer):
        result = hanzi_decomposer.get_radical_meaning('一')
        assert result == 'one'
