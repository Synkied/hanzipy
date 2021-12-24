# coding:utf-8
from pathlib import Path

from hanzipy.dictionary import HanziDictionary

import pytest

CURRENT_DIR = BASE_DIR = Path(__file__).parent.parent


@pytest.fixture
def hanzi_dictionary():
    return HanziDictionary()


class TestDictionary:
    def test_dictionary_search(self, hanzi_dictionary):
        definition_keys = ['traditional', 'simplified', 'pinyin', 'definition']
        result = hanzi_dictionary.dictionary_search('句')

        assert list(result[0].keys()) == definition_keys
        assert result == [
            {
                'traditional': '一句',
                'simplified': '一句',
                'pinyin': 'yi1 ju4',
                'definition': 'a line of verse/a sentence'
            },
            {
                'traditional': '一句話',
                'simplified': '一句话',
                'pinyin': 'yi1 ju4 hua4',
                'definition': 'in a word/in short'
            },
            {
                'traditional': '三句話不離本行',
                'simplified': '三句话不离本行',
                'pinyin': 'san1 ju4 hua4 bu4 li2 ben3 hang2',
                'definition': 'to talk shop all the time (idiom)'
            },
            {
                'traditional': '三言兩句',
                'simplified': '三言两句',
                'pinyin': 'san1 yan2 liang3 ju4',
                'definition': 'in a few words (idiom); expressed succinctly'
            },
            {
                'traditional': '中心埋置關係從句',
                'simplified': '中心埋置关系从句',
                'pinyin': 'zhong1 xin1 mai2 zhi4 guan1 xi4 cong2 ju4',
                'definition': 'center-embedded relative clauses'
            },
            {
                'traditional': '主謂句',
                'simplified': '主谓句',
                'pinyin': 'zhu3 wei4 ju4',
                'definition':
                'subject-predicate sentence/subject-predicate clause'
            },
            {
                'traditional':
                '五言絕句',
                'simplified':
                '五言绝句',
                'pinyin':
                'wu3 yan2 jue2 ju4',
                'definition':
                'poetic form consisting of four lines of five syllables, with rhymes on first, second and fourth line'  # noqa
            },
            {
                'traditional': '例句',
                'simplified': '例句',
                'pinyin': 'li4 ju4',
                'definition': 'example sentence'
            },
            {
                'traditional': '俳句',
                'simplified': '俳句',
                'pinyin': 'pai2 ju4',
                'definition': 'haiku'
            },
            {
                'traditional':
                '倒裝句',
                'simplified':
                '倒装句',
                'pinyin':
                'dao4 zhuang1 ju4',
                'definition':
                'inversion (rhetoric device of inverting the word order for heightened effect)/anastrophe'  # noqa
            },
            {
                'traditional': '假肯定句',
                'simplified': '假肯定句',
                'pinyin': 'jia3 ken3 ding4 ju4',
                'definition': 'false affirmative'
            },
            {
                'traditional': '兩句',
                'simplified': '两句',
                'pinyin': 'liang3 ju4',
                'definition': '(say) a few words'
            },
            {
                'traditional': '分句',
                'simplified': '分句',
                'pinyin': 'fen1 ju4',
                'definition': 'clause (grammar)'
            },
            {
                'traditional': '反問句',
                'simplified': '反问句',
                'pinyin': 'fan3 wen4 ju4',
                'definition': 'rhetorical question'
            },
            {
                'traditional': '句',
                'simplified': '句',
                'pinyin': 'gou1',
                'definition': 'variant of 勾[gou1]'
            },
            {
                'traditional':
                '句',
                'simplified':
                '句',
                'pinyin':
                'ju4',
                'definition':
                'sentence/clause/phrase/classifier for phrases or lines of verse'  # noqa
            },
            {
                'traditional':
                '句',
                'simplified':
                '句',
                'pinyin':
                'ju4',
                'definition':
                'sentence/clause/phrase/classifier for phrases or lines of verse'  # noqa
            },
            {
                'traditional': '句句實話',
                'simplified': '句句实话',
                'pinyin': 'ju4 ju4 shi2 hua4',
                'definition': 'to speak honestly (idiom)'
            },
            {
                'traditional': '句型',
                'simplified': '句型',
                'pinyin': 'ju4 xing2',
                'definition': 'sentence pattern (in grammar)'
            },
            {
                'traditional': '句子',
                'simplified': '句子',
                'pinyin': 'ju4 zi5',
                'definition': 'sentence/CL:個|个[ge4]'
            },
            {
                'traditional':
                '句容',
                'simplified':
                '句容',
                'pinyin':
                'Ju4 rong2',
                'definition':
                'Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu'  # noqa
            },
            {
                'traditional':
                '句容市',
                'simplified':
                '句容市',
                'pinyin':
                'Ju4 rong2 shi4',
                'definition':
                'Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu'  # noqa
            },
            {
                'traditional': '句式',
                'simplified': '句式',
                'pinyin': 'ju4 shi4',
                'definition': 'sentence pattern/sentence structure/syntax'
            },
            {
                'traditional': '句數',
                'simplified': '句数',
                'pinyin': 'ju4 shu4',
                'definition':
                'number of sentences/number of lines (in verse etc)'
            },
            {
                'traditional': '句法',
                'simplified': '句法',
                'pinyin': 'ju4 fa3',
                'definition': 'syntax'
            },
            {
                'traditional': '句法分析',
                'simplified': '句法分析',
                'pinyin': 'ju4 fa3 fen1 xi1',
                'definition': 'syntactic analysis'
            },
            {
                'traditional': '句法意識',
                'simplified': '句法意识',
                'pinyin': 'ju4 fa3 yi4 shi2',
                'definition': 'syntactic awareness'
            },
            {
                'traditional':
                '句群',
                'simplified':
                '句群',
                'pinyin':
                'ju4 qun2',
                'definition':
                'discourse/group of sentences with clear meaning/narrative'
            },
            {
                'traditional': '句號',
                'simplified': '句号',
                'pinyin': 'ju4 hao4',
                'definition': 'full stop/period (punct.)'
            },
            {
                'traditional':
                '句讀',
                'simplified':
                '句读',
                'pinyin':
                'ju4 dou4',
                'definition':
                'pausing at the end of a phrase or sentence (in former times, before punctuation marks were used)/punctuation/periods and commas/sentences and phrases'  # noqa
            },
            {
                'traditional':
                '句逗',
                'simplified':
                '句逗',
                'pinyin':
                'ju4 dou4',
                'definition':
                'punctuation of a sentence (in former times, before punctuation marks were used)/period 句號|句号 and comma 逗號|逗号/sentences and phrases'  # noqa
            },
            {
                'traditional': '句首',
                'simplified': '句首',
                'pinyin': 'ju4 shou3',
                'definition': 'start of phrase or sentence'
            },
            {
                'traditional': '句驪河',
                'simplified': '句骊河',
                'pinyin': 'Ju4 li2 He2',
                'definition': 'pre-Han name of Liao River 遼河|辽河[Liao2 He2]'
            },
            {
                'traditional': '句點',
                'simplified': '句点',
                'pinyin': 'ju4 dian3',
                'definition': 'period (punctuation)/(fig.) endpoint/finish'
            },
            {
                'traditional': '名句',
                'simplified': '名句',
                'pinyin': 'ming2 ju4',
                'definition': 'famous saying/celebrated phrase'
            },
            {
                'traditional': '否定句',
                'simplified': '否定句',
                'pinyin': 'fou3 ding4 ju4',
                'definition': 'negative sentence'
            },
            {
                'traditional': '命令句',
                'simplified': '命令句',
                'pinyin': 'ming4 ling4 ju4',
                'definition': 'imperative sentence'
            },
            {
                'traditional': '單句',
                'simplified': '单句',
                'pinyin': 'dan1 ju4',
                'definition': 'simple sentence (grammar)'
            },
            {
                'traditional': '子句',
                'simplified': '子句',
                'pinyin': 'zi3 ju4',
                'definition': 'clause (grammar)'
            },
            {
                'traditional': '字句',
                'simplified': '字句',
                'pinyin': 'zi4 ju4',
                'definition': 'words/expressions/writing'
            },
            {
                'traditional': '字斟句酌',
                'simplified': '字斟句酌',
                'pinyin': 'zi4 zhen1 ju4 zhuo2',
                'definition': 'weighing every word'
            },
            {
                'traditional': '對句',
                'simplified': '对句',
                'pinyin': 'dui4 ju2',
                'definition': 'couplet'
            },
            {
                'traditional': '引用句',
                'simplified': '引用句',
                'pinyin': 'yin3 yong4 ju4',
                'definition': 'quotation'
            },
            {
                'traditional': '從句',
                'simplified': '从句',
                'pinyin': 'cong2 ju4',
                'definition': 'clause'
            },
            {
                'traditional': '感嘆句',
                'simplified': '感叹句',
                'pinyin': 'gan3 tan4 ju4',
                'definition': 'exclamation/exclamatory phrase'
            },
            {
                'traditional': '換句話說',
                'simplified': '换句话说',
                'pinyin': 'huan4 ju4 hua4 shuo1',
                'definition': 'in other words'
            },
            {
                'traditional': '斟酌字句',
                'simplified': '斟酌字句',
                'pinyin': 'zhen1 zhuo2 zi4 ju4',
                'definition': "to measure one's words"
            },
            {
                'traditional':
                '斷句',
                'simplified':
                '断句',
                'pinyin':
                'duan4 ju4',
                'definition':
                'to pause at appropriate points in reading aloud unpunctuated writing/to punctuate'  # noqa
            },
            {
                'traditional': '有一句沒一句',
                'simplified': '有一句没一句',
                'pinyin': 'you3 yi1 ju4 mei2 yi1 ju4',
                'definition': 'to speak one minute and be quiet the next'
            },
            {
                'traditional': '條件句',
                'simplified': '条件句',
                'pinyin': 'tiao2 jian4 ju4',
                'definition': 'conditional clause'
            },
            {
                'traditional': '樂句',
                'simplified': '乐句',
                'pinyin': 'yue4 ju4',
                'definition': 'musical phrase'
            },
            {
                'traditional': '煉句',
                'simplified': '炼句',
                'pinyin': 'lian4 ju4',
                'definition': 'to polish a phrase'
            },
            {
                'traditional': '特指問句',
                'simplified': '特指问句',
                'pinyin': 'te4 zhi3 wen4 ju4',
                'definition': 'wh-question (linguistics)'
            },
            {
                'traditional': '獨語句',
                'simplified': '独语句',
                'pinyin': 'du2 yu3 ju4',
                'definition': 'one-word sentence'
            },
            {
                'traditional': '疑問句',
                'simplified': '疑问句',
                'pinyin': 'yi2 wen4 ju4',
                'definition': 'question (grammar)/interrogative sentence'
            },
            {
                'traditional': '病句',
                'simplified': '病句',
                'pinyin': 'bing4 ju4',
                'definition': 'defective sentence/error (of grammar or logic)'
            },
            {
                'traditional': '真否定句',
                'simplified': '真否定句',
                'pinyin': 'zhen1 fou3 ding4 ju4',
                'definition': 'true negative (TN)'
            },
            {
                'traditional': '真肯定句',
                'simplified': '真肯定句',
                'pinyin': 'zhen1 ken3 ding4 ju4',
                'definition': 'true affirmative (TA)'
            },
            {
                'traditional': '短句',
                'simplified': '短句',
                'pinyin': 'duan3 ju4',
                'definition': 'clause'
            },
            {
                'traditional': '祈使句',
                'simplified': '祈使句',
                'pinyin': 'qi2 shi3 ju4',
                'definition': 'imperative sentence'
            },
            {
                'traditional': '絕句',
                'simplified': '绝句',
                'pinyin': 'jue2 ju4',
                'definition': 'quatrain (poetic form)'
            },
            {
                'traditional': '肯定並例句',
                'simplified': '肯定并例句',
                'pinyin': 'ken3 ding4 bing4 li4 ju4',
                'definition': 'active conjoined sentence'
            },
            {
                'traditional': '肯定句',
                'simplified': '肯定句',
                'pinyin': 'ken3 ding4 ju4',
                'definition': 'affirmative sentence'
            },
            {
                'traditional': '複句',
                'simplified': '复句',
                'pinyin': 'fu4 ju4',
                'definition': 'compound phrase'
            },
            {
                'traditional': '覓句',
                'simplified': '觅句',
                'pinyin': 'mi4 ju4',
                'definition': 'to search for the right word (of poet)'
            },
            {
                'traditional': '詞句',
                'simplified': '词句',
                'pinyin': 'ci2 ju4',
                'definition': 'words and sentences'
            },
            {
                'traditional': '詩句',
                'simplified': '诗句',
                'pinyin': 'shi1 ju4',
                'definition': 'verse/CL:行[hang2]'
            },
            {
                'traditional':
                '話不投機半句多',
                'simplified':
                '话不投机半句多',
                'pinyin':
                'hua4 bu4 tou2 ji1 ban4 ju4 duo1',
                'definition':
                "when views are irreconcilable, it's a waste of breath to continue discussion (idiom)"  # noqa
            },
            {
                'traditional': '語句',
                'simplified': '语句',
                'pinyin': 'yu3 ju4',
                'definition': 'sentence'
            },
            {
                'traditional': '警句',
                'simplified': '警句',
                'pinyin': 'jing3 ju4',
                'definition': 'aphorism'
            },
            {
                'traditional':
                '讀破句',
                'simplified':
                '读破句',
                'pinyin':
                'du2 po4 ju4',
                'definition':
                'incorrect break in reading Chinese, dividing text into clauses at wrong point'  # noqa
            },
            {
                'traditional': '賓語關係從句',
                'simplified': '宾语关系从句',
                'pinyin': 'bin1 yu3 guan1 xi4 cong2 ju4',
                'definition': 'object relative clause'
            },
            {
                'traditional': '逐字逐句',
                'simplified': '逐字逐句',
                'pinyin': 'zhu2 zi4 zhu2 ju4',
                'definition': 'literal/word by word and phrase by phrase'
            },
            {
                'traditional': '造句',
                'simplified': '造句',
                'pinyin': 'zao4 ju4',
                'definition': 'sentence-making'
            },
            {
                'traditional':
                '閉門覓句',
                'simplified':
                '闭门觅句',
                'pinyin':
                'bi4 men2 mi4 ju4',
                'definition':
                'lit. lock the door and search for the right word (idiom); fig. the serious hard work of writing'  # noqa
            },
            {
                'traditional': '陳述句',
                'simplified': '陈述句',
                'pinyin': 'chen2 shu4 ju4',
                'definition': 'declarative sentence'
            },
            {
                'traditional':
                '高句麗',
                'simplified':
                '高句丽',
                'pinyin':
                'Gao1 gou1 li2',
                'definition':
                'Goguryeo (37 BC-668 AD), one of the Korean Three Kingdoms'
            }
        ]

    def test_get_examples(self, hanzi_dictionary):
        freq_keys = ['high_frequency', 'mid_frequency', 'low_frequency']
        result = hanzi_dictionary.get_examples('句')

        assert list(result.keys()) == freq_keys
        assert result == {
            'high_frequency': [{
                'traditional': '句',
                'simplified': '句',
                'pinyin': 'gou1',
                'definition': 'variant of 勾[gou1]'
            }, {
                'traditional':
                '句',
                'simplified':
                '句',
                'pinyin':
                'ju4',
                'definition':
                'sentence/clause/phrase/classifier for phrases or lines of verse'  # noqa
            }, {
                'traditional':
                '句',
                'simplified':
                '句',
                'pinyin':
                'ju4',
                'definition':
                'sentence/clause/phrase/classifier for phrases or lines of verse'  # noqa
            }],
            'mid_frequency': [{
                'traditional': '句子',
                'simplified': '句子',
                'pinyin': 'ju4 zi5',
                'definition': 'sentence/CL:個|个[ge4]'
            }],
            'low_frequency': [{
                'traditional': '一句',
                'simplified': '一句',
                'pinyin': 'yi1 ju4',
                'definition': 'a line of verse/a sentence'
            }, {
                'traditional': '例句',
                'simplified': '例句',
                'pinyin': 'li4 ju4',
                'definition': 'example sentence'
            }, {
                'traditional': '俳句',
                'simplified': '俳句',
                'pinyin': 'pai2 ju4',
                'definition': 'haiku'
            }, {
                'traditional': '分句',
                'simplified': '分句',
                'pinyin': 'fen1 ju4',
                'definition': 'clause (grammar)'
            }, {
                'traditional': '反問句',
                'simplified': '反问句',
                'pinyin': 'fan3 wen4 ju4',
                'definition': 'rhetorical question'
            }, {
                'traditional': '句型',
                'simplified': '句型',
                'pinyin': 'ju4 xing2',
                'definition': 'sentence pattern (in grammar)'
            }, {
                'traditional':
                '句容',
                'simplified':
                '句容',
                'pinyin':
                'Ju4 rong2',
                'definition':
                'Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu'  # noqa
            }, {
                'traditional':
                '句容市',
                'simplified':
                '句容市',
                'pinyin':
                'Ju4 rong2 shi4',
                'definition':
                'Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu'  # noqa
            }, {
                'traditional':
                '句式',
                'simplified':
                '句式',
                'pinyin':
                'ju4 shi4',
                'definition':
                'sentence pattern/sentence structure/syntax'
            }, {
                'traditional': '句法',
                'simplified': '句法',
                'pinyin': 'ju4 fa3',
                'definition': 'syntax'
            }, {
                'traditional': '句號',
                'simplified': '句号',
                'pinyin': 'ju4 hao4',
                'definition': 'full stop/period (punct.)'
            }, {
                'traditional':
                '句點',
                'simplified':
                '句点',
                'pinyin':
                'ju4 dian3',
                'definition':
                'period (punctuation)/(fig.) endpoint/finish'
            }, {
                'traditional': '名句',
                'simplified': '名句',
                'pinyin': 'ming2 ju4',
                'definition': 'famous saying/celebrated phrase'
            }, {
                'traditional': '字句',
                'simplified': '字句',
                'pinyin': 'zi4 ju4',
                'definition': 'words/expressions/writing'
            }, {
                'traditional': '字斟句酌',
                'simplified': '字斟句酌',
                'pinyin': 'zi4 zhen1 ju4 zhuo2',
                'definition': 'weighing every word'
            }, {
                'traditional': '對句',
                'simplified': '对句',
                'pinyin': 'dui4 ju2',
                'definition': 'couplet'
            }, {
                'traditional': '從句',
                'simplified': '从句',
                'pinyin': 'cong2 ju4',
                'definition': 'clause'
            }, {
                'traditional': '感嘆句',
                'simplified': '感叹句',
                'pinyin': 'gan3 tan4 ju4',
                'definition': 'exclamation/exclamatory phrase'
            }, {
                'traditional': '換句話說',
                'simplified': '换句话说',
                'pinyin': 'huan4 ju4 hua4 shuo1',
                'definition': 'in other words'
            }, {
                'traditional':
                '斷句',
                'simplified':
                '断句',
                'pinyin':
                'duan4 ju4',
                'definition':
                'to pause at appropriate points in reading aloud unpunctuated writing/to punctuate'  # noqa
            }, {
                'traditional': '樂句',
                'simplified': '乐句',
                'pinyin': 'yue4 ju4',
                'definition': 'musical phrase'
            }, {
                'traditional':
                '疑問句',
                'simplified':
                '疑问句',
                'pinyin':
                'yi2 wen4 ju4',
                'definition':
                'question (grammar)/interrogative sentence'
            }, {
                'traditional':
                '病句',
                'simplified':
                '病句',
                'pinyin':
                'bing4 ju4',
                'definition':
                'defective sentence/error (of grammar or logic)'
            }, {
                'traditional': '短句',
                'simplified': '短句',
                'pinyin': 'duan3 ju4',
                'definition': 'clause'
            }, {
                'traditional': '祈使句',
                'simplified': '祈使句',
                'pinyin': 'qi2 shi3 ju4',
                'definition': 'imperative sentence'
            }, {
                'traditional': '絕句',
                'simplified': '绝句',
                'pinyin': 'jue2 ju4',
                'definition': 'quatrain (poetic form)'
            }, {
                'traditional': '詞句',
                'simplified': '词句',
                'pinyin': 'ci2 ju4',
                'definition': 'words and sentences'
            }, {
                'traditional': '詩句',
                'simplified': '诗句',
                'pinyin': 'shi1 ju4',
                'definition': 'verse/CL:行[hang2]'
            }, {
                'traditional': '語句',
                'simplified': '语句',
                'pinyin': 'yu3 ju4',
                'definition': 'sentence'
            }, {
                'traditional': '警句',
                'simplified': '警句',
                'pinyin': 'jing3 ju4',
                'definition': 'aphorism'
            }, {
                'traditional': '造句',
                'simplified': '造句',
                'pinyin': 'zao4 ju4',
                'definition': 'sentence-making'
            }, {
                'traditional': '陳述句',
                'simplified': '陈述句',
                'pinyin': 'chen2 shu4 ju4',
                'definition': 'declarative sentence'
            }, {
                'traditional':
                '高句麗',
                'simplified':
                '高句丽',
                'pinyin':
                'Gao1 gou1 li2',
                'definition':
                'Goguryeo (37 BC-668 AD), one of the Korean Three Kingdoms'
            }]
        }

    def test_determine_if_simplfied_char(self, hanzi_dictionary):
        simplified_char = hanzi_dictionary.determine_if_simplfied_char('句')
        traditional_char = hanzi_dictionary.determine_if_simplfied_char('學')

        assert simplified_char is True
        assert traditional_char is False

    def test_get_pinyin(self, hanzi_dictionary):
        result = hanzi_dictionary.get_pinyin('句')
        assert result == ['ju4', 'ju4', 'gou1']

        result = hanzi_dictionary.get_pinyin('學')
        assert result == ['xue2']
