# coding:utf-8
from pathlib import Path

from hanzipy.dictionary import HanziDictionary
from hanzipy.exceptions import NotAHanziCharacter

import pytest

CURRENT_DIR = BASE_DIR = Path(__file__).parent.parent


@pytest.fixture
def hanzi_dictionary():
    return HanziDictionary()


class TestDictionary:
    def test_dictionary_search(self, hanzi_dictionary):
        definition_keys = ["traditional", "simplified", "pinyin", "definition"]
        result = hanzi_dictionary.dictionary_search("句")

        assert list(result[0].keys()) == definition_keys
        assert result == [
            {
                "traditional": "一句",
                "simplified": "一句",
                "pinyin": "yi1 ju4",
                "definition": "a line of verse/a sentence",
            },
            {
                "traditional": "一句話",
                "simplified": "一句话",
                "pinyin": "yi1 ju4 hua4",
                "definition": "in a word/in short",
            },
            {
                "traditional": "三句話不離本行",
                "simplified": "三句话不离本行",
                "pinyin": "san1 ju4 hua4 bu4 li2 ben3 hang2",
                "definition": "to talk shop all the time (idiom)",
            },
            {
                "traditional": "三言兩句",
                "simplified": "三言两句",
                "pinyin": "san1 yan2 liang3 ju4",
                "definition": "in a few words (idiom); expressed succinctly",
            },
            {
                "traditional": "中心埋置關係從句",
                "simplified": "中心埋置关系从句",
                "pinyin": "zhong1 xin1 mai2 zhi4 guan1 xi4 cong2 ju4",
                "definition": "center-embedded relative clauses",
            },
            {
                "traditional": "主謂句",
                "simplified": "主谓句",
                "pinyin": "zhu3 wei4 ju4",
                "definition": "subject-predicate sentence/subject-predicate clause",
            },
            {
                "traditional": "五言絕句",
                "simplified": "五言绝句",
                "pinyin": "wu3 yan2 jue2 ju4",
                "definition": "poetic form consisting of four lines of five syllables, with rhymes on first, second and fourth line",  # noqa
            },
            {
                "traditional": "例句",
                "simplified": "例句",
                "pinyin": "li4 ju4",
                "definition": "example sentence",
            },
            {
                "traditional": "俳句",
                "simplified": "俳句",
                "pinyin": "pai2 ju4",
                "definition": "haiku",
            },
            {
                "traditional": "倒裝句",
                "simplified": "倒装句",
                "pinyin": "dao4 zhuang1 ju4",
                "definition": "inversion (rhetoric device of inverting the word order for heightened effect)/anastrophe",  # noqa
            },
            {
                "traditional": "假肯定句",
                "simplified": "假肯定句",
                "pinyin": "jia3 ken3 ding4 ju4",
                "definition": "false affirmative",
            },
            {
                "traditional": "兩句",
                "simplified": "两句",
                "pinyin": "liang3 ju4",
                "definition": "(say) a few words",
            },
            {
                "traditional": "分句",
                "simplified": "分句",
                "pinyin": "fen1 ju4",
                "definition": "clause (grammar)",
            },
            {
                "traditional": "反問句",
                "simplified": "反问句",
                "pinyin": "fan3 wen4 ju4",
                "definition": "rhetorical question",
            },
            {
                "traditional": "句",
                "simplified": "句",
                "pinyin": "gou1",
                "definition": "variant of 勾[gou1]",
            },
            {
                "traditional": "句",
                "simplified": "句",
                "pinyin": "ju4",
                "definition": "sentence/clause/phrase/classifier for phrases or lines of verse",  # noqa
            },
            {
                "traditional": "句句實話",
                "simplified": "句句实话",
                "pinyin": "ju4 ju4 shi2 hua4",
                "definition": "to speak honestly (idiom)",
            },
            {
                "traditional": "句型",
                "simplified": "句型",
                "pinyin": "ju4 xing2",
                "definition": "sentence pattern (in grammar)",
            },
            {
                "traditional": "句子",
                "simplified": "句子",
                "pinyin": "ju4 zi5",
                "definition": "sentence/CL:個|个[ge4]",
            },
            {
                "traditional": "句容",
                "simplified": "句容",
                "pinyin": "Ju4 rong2",
                "definition": "Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu",  # noqa
            },
            {
                "traditional": "句容市",
                "simplified": "句容市",
                "pinyin": "Ju4 rong2 shi4",
                "definition": "Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu",  # noqa
            },
            {
                "traditional": "句式",
                "simplified": "句式",
                "pinyin": "ju4 shi4",
                "definition": "sentence pattern/sentence structure/syntax",
            },
            {
                "traditional": "句數",
                "simplified": "句数",
                "pinyin": "ju4 shu4",
                "definition": "number of sentences/number of lines (in verse etc)",
            },
            {
                "traditional": "句法",
                "simplified": "句法",
                "pinyin": "ju4 fa3",
                "definition": "syntax",
            },
            {
                "traditional": "句法分析",
                "simplified": "句法分析",
                "pinyin": "ju4 fa3 fen1 xi1",
                "definition": "syntactic analysis",
            },
            {
                "traditional": "句法意識",
                "simplified": "句法意识",
                "pinyin": "ju4 fa3 yi4 shi2",
                "definition": "syntactic awareness",
            },
            {
                "traditional": "句群",
                "simplified": "句群",
                "pinyin": "ju4 qun2",
                "definition": "discourse/group of sentences with clear meaning/narrative",
            },
            {
                "traditional": "句號",
                "simplified": "句号",
                "pinyin": "ju4 hao4",
                "definition": "full stop/period (punct.)",
            },
            {
                "traditional": "句讀",
                "simplified": "句读",
                "pinyin": "ju4 dou4",
                "definition": "pausing at the end of a phrase or sentence (in former times, before punctuation marks were used)/punctuation/periods and commas/sentences and phrases",  # noqa
            },
            {
                "traditional": "句逗",
                "simplified": "句逗",
                "pinyin": "ju4 dou4",
                "definition": "punctuation of a sentence (in former times, before punctuation marks were used)/period 句號|句号 and comma 逗號|逗号/sentences and phrases",  # noqa
            },
            {
                "traditional": "句首",
                "simplified": "句首",
                "pinyin": "ju4 shou3",
                "definition": "start of phrase or sentence",
            },
            {
                "traditional": "句驪河",
                "simplified": "句骊河",
                "pinyin": "Ju4 li2 He2",
                "definition": "pre-Han name of Liao River 遼河|辽河[Liao2 He2]",
            },
            {
                "traditional": "句點",
                "simplified": "句点",
                "pinyin": "ju4 dian3",
                "definition": "period (punctuation)/(fig.) endpoint/finish",
            },
            {
                "traditional": "名句",
                "simplified": "名句",
                "pinyin": "ming2 ju4",
                "definition": "famous saying/celebrated phrase",
            },
            {
                "traditional": "否定句",
                "simplified": "否定句",
                "pinyin": "fou3 ding4 ju4",
                "definition": "negative sentence",
            },
            {
                "traditional": "命令句",
                "simplified": "命令句",
                "pinyin": "ming4 ling4 ju4",
                "definition": "imperative sentence",
            },
            {
                "traditional": "單句",
                "simplified": "单句",
                "pinyin": "dan1 ju4",
                "definition": "simple sentence (grammar)",
            },
            {
                "traditional": "子句",
                "simplified": "子句",
                "pinyin": "zi3 ju4",
                "definition": "clause (grammar)",
            },
            {
                "traditional": "字句",
                "simplified": "字句",
                "pinyin": "zi4 ju4",
                "definition": "words/expressions/writing",
            },
            {
                "traditional": "字斟句酌",
                "simplified": "字斟句酌",
                "pinyin": "zi4 zhen1 ju4 zhuo2",
                "definition": "weighing every word",
            },
            {
                "traditional": "對句",
                "simplified": "对句",
                "pinyin": "dui4 ju2",
                "definition": "couplet",
            },
            {
                "traditional": "引用句",
                "simplified": "引用句",
                "pinyin": "yin3 yong4 ju4",
                "definition": "quotation",
            },
            {
                "traditional": "從句",
                "simplified": "从句",
                "pinyin": "cong2 ju4",
                "definition": "clause",
            },
            {
                "traditional": "感嘆句",
                "simplified": "感叹句",
                "pinyin": "gan3 tan4 ju4",
                "definition": "exclamation/exclamatory phrase",
            },
            {
                "traditional": "換句話說",
                "simplified": "换句话说",
                "pinyin": "huan4 ju4 hua4 shuo1",
                "definition": "in other words",
            },
            {
                "traditional": "斟酌字句",
                "simplified": "斟酌字句",
                "pinyin": "zhen1 zhuo2 zi4 ju4",
                "definition": "to measure one's words",
            },
            {
                "traditional": "斷句",
                "simplified": "断句",
                "pinyin": "duan4 ju4",
                "definition": "to pause at appropriate points in reading aloud unpunctuated writing/to punctuate",  # noqa
            },
            {
                "traditional": "有一句沒一句",
                "simplified": "有一句没一句",
                "pinyin": "you3 yi1 ju4 mei2 yi1 ju4",
                "definition": "to speak one minute and be quiet the next",
            },
            {
                "traditional": "條件句",
                "simplified": "条件句",
                "pinyin": "tiao2 jian4 ju4",
                "definition": "conditional clause",
            },
            {
                "traditional": "樂句",
                "simplified": "乐句",
                "pinyin": "yue4 ju4",
                "definition": "musical phrase",
            },
            {
                "traditional": "煉句",
                "simplified": "炼句",
                "pinyin": "lian4 ju4",
                "definition": "to polish a phrase",
            },
            {
                "traditional": "特指問句",
                "simplified": "特指问句",
                "pinyin": "te4 zhi3 wen4 ju4",
                "definition": "wh-question (linguistics)",
            },
            {
                "traditional": "獨語句",
                "simplified": "独语句",
                "pinyin": "du2 yu3 ju4",
                "definition": "one-word sentence",
            },
            {
                "traditional": "疑問句",
                "simplified": "疑问句",
                "pinyin": "yi2 wen4 ju4",
                "definition": "question (grammar)/interrogative sentence",
            },
            {
                "traditional": "病句",
                "simplified": "病句",
                "pinyin": "bing4 ju4",
                "definition": "defective sentence/error (of grammar or logic)",
            },
            {
                "traditional": "真否定句",
                "simplified": "真否定句",
                "pinyin": "zhen1 fou3 ding4 ju4",
                "definition": "true negative (TN)",
            },
            {
                "traditional": "真肯定句",
                "simplified": "真肯定句",
                "pinyin": "zhen1 ken3 ding4 ju4",
                "definition": "true affirmative (TA)",
            },
            {
                "traditional": "短句",
                "simplified": "短句",
                "pinyin": "duan3 ju4",
                "definition": "clause",
            },
            {
                "traditional": "祈使句",
                "simplified": "祈使句",
                "pinyin": "qi2 shi3 ju4",
                "definition": "imperative sentence",
            },
            {
                "traditional": "絕句",
                "simplified": "绝句",
                "pinyin": "jue2 ju4",
                "definition": "quatrain (poetic form)",
            },
            {
                "traditional": "肯定並例句",
                "simplified": "肯定并例句",
                "pinyin": "ken3 ding4 bing4 li4 ju4",
                "definition": "active conjoined sentence",
            },
            {
                "traditional": "肯定句",
                "simplified": "肯定句",
                "pinyin": "ken3 ding4 ju4",
                "definition": "affirmative sentence",
            },
            {
                "traditional": "複句",
                "simplified": "复句",
                "pinyin": "fu4 ju4",
                "definition": "compound phrase",
            },
            {
                "traditional": "覓句",
                "simplified": "觅句",
                "pinyin": "mi4 ju4",
                "definition": "to search for the right word (of poet)",
            },
            {
                "traditional": "詞句",
                "simplified": "词句",
                "pinyin": "ci2 ju4",
                "definition": "words and sentences",
            },
            {
                "traditional": "詩句",
                "simplified": "诗句",
                "pinyin": "shi1 ju4",
                "definition": "verse/CL:行[hang2]",
            },
            {
                "traditional": "話不投機半句多",
                "simplified": "话不投机半句多",
                "pinyin": "hua4 bu4 tou2 ji1 ban4 ju4 duo1",
                "definition": "when views are irreconcilable, it's a waste of breath to continue discussion (idiom)",  # noqa
            },
            {
                "traditional": "語句",
                "simplified": "语句",
                "pinyin": "yu3 ju4",
                "definition": "sentence",
            },
            {
                "traditional": "警句",
                "simplified": "警句",
                "pinyin": "jing3 ju4",
                "definition": "aphorism",
            },
            {
                "traditional": "讀破句",
                "simplified": "读破句",
                "pinyin": "du2 po4 ju4",
                "definition": "incorrect break in reading Chinese, dividing text into clauses at wrong point",  # noqa
            },
            {
                "traditional": "賓語關係從句",
                "simplified": "宾语关系从句",
                "pinyin": "bin1 yu3 guan1 xi4 cong2 ju4",
                "definition": "object relative clause",
            },
            {
                "traditional": "逐字逐句",
                "simplified": "逐字逐句",
                "pinyin": "zhu2 zi4 zhu2 ju4",
                "definition": "literal/word by word and phrase by phrase",
            },
            {
                "traditional": "造句",
                "simplified": "造句",
                "pinyin": "zao4 ju4",
                "definition": "sentence-making",
            },
            {
                "traditional": "閉門覓句",
                "simplified": "闭门觅句",
                "pinyin": "bi4 men2 mi4 ju4",
                "definition": "lit. lock the door and search for the right word (idiom); fig. the serious hard work of writing",  # noqa
            },
            {
                "traditional": "陳述句",
                "simplified": "陈述句",
                "pinyin": "chen2 shu4 ju4",
                "definition": "declarative sentence",
            },
            {
                "traditional": "高句麗",
                "simplified": "高句丽",
                "pinyin": "Gao1 gou1 li2",
                "definition": "Goguryeo (37 BC-668 AD), one of the Korean Three Kingdoms",
            },
        ]

        result = hanzi_dictionary.dictionary_search("心的小孩真", "only")
        assert result == [
            {
                "traditional": "孩",
                "simplified": "孩",
                "pinyin": "hai2",
                "definition": "child",
            },
            {
                "traditional": "小",
                "simplified": "小",
                "pinyin": "xiao3",
                "definition": "small/tiny/few/young",
            },
            {
                "traditional": "小孩",
                "simplified": "小孩",
                "pinyin": "xiao3 hai2",
                "definition": "child/CL:個|个[ge4]",
            },
            {
                "traditional": "小小",
                "simplified": "小小",
                "pinyin": "xiao3 xiao3",
                "definition": "very small/very few/very minor",
            },
            {
                "traditional": "小心",
                "simplified": "小心",
                "pinyin": "xiao3 xin1",
                "definition": "to be careful/to take care",
            },
            {
                "traditional": "小的",
                "simplified": "小的",
                "pinyin": "xiao3 de5",
                "definition": "I (when talking to a superior)",
            },
            {
                "traditional": "心",
                "simplified": "心",
                "pinyin": "xin1",
                "definition": "heart/mind/intention/center/core/CL:顆|颗[ke1],個|个[ge4]",
            },
            {
                "traditional": "的",
                "simplified": "的",
                "pinyin": "de5",
                "definition": "of/~'s (possessive particle)/(used after an attribute)/(used to form a nominal expression)/(used at the end of a declarative sentence for emphasis)/also pr. [di4] or [di5] in poetry and songs",
            },
            {
                "traditional": "的",
                "simplified": "的",
                "pinyin": "di1",
                "definition": "see 的士[di1 shi4]",
            },
            {
                "traditional": "的",
                "simplified": "的",
                "pinyin": "di2",
                "definition": "really and truly",
            },
            {
                "traditional": "的",
                "simplified": "的",
                "pinyin": "di4",
                "definition": "aim/clear",
            },
            {
                "traditional": "真",
                "simplified": "真",
                "pinyin": "zhen1",
                "definition": "really/truly/indeed/real/true/genuine",
            },
            {
                "traditional": "真心",
                "simplified": "真心",
                "pinyin": "zhen1 xin1",
                "definition": "sincere/heartfelt/CL:片[pian4]",
            },
            {
                "traditional": "真真",
                "simplified": "真真",
                "pinyin": "zhen1 zhen1",
                "definition": "really/in fact/genuinely/scrupulously",
            },
        ]

    def test_get_examples(self, hanzi_dictionary):
        freq_keys = ["high_frequency", "mid_frequency", "low_frequency"]
        result = hanzi_dictionary.get_examples("句")

        assert list(result.keys()) == freq_keys
        assert result == {
            "high_frequency": [
                {
                    "traditional": "句",
                    "simplified": "句",
                    "pinyin": "gou1",
                    "definition": "variant of 勾[gou1]",
                },
                {
                    "traditional": "句",
                    "simplified": "句",
                    "pinyin": "ju4",
                    "definition": "sentence/clause/phrase/classifier for phrases or lines of verse",  # noqa
                },
            ],
            "mid_frequency": [
                {
                    "traditional": "句子",
                    "simplified": "句子",
                    "pinyin": "ju4 zi5",
                    "definition": "sentence/CL:個|个[ge4]",
                }
            ],
            "low_frequency": [
                {
                    "traditional": "一句",
                    "simplified": "一句",
                    "pinyin": "yi1 ju4",
                    "definition": "a line of verse/a sentence",
                },
                {
                    "traditional": "例句",
                    "simplified": "例句",
                    "pinyin": "li4 ju4",
                    "definition": "example sentence",
                },
                {
                    "traditional": "俳句",
                    "simplified": "俳句",
                    "pinyin": "pai2 ju4",
                    "definition": "haiku",
                },
                {
                    "traditional": "分句",
                    "simplified": "分句",
                    "pinyin": "fen1 ju4",
                    "definition": "clause (grammar)",
                },
                {
                    "traditional": "反問句",
                    "simplified": "反问句",
                    "pinyin": "fan3 wen4 ju4",
                    "definition": "rhetorical question",
                },
                {
                    "traditional": "句型",
                    "simplified": "句型",
                    "pinyin": "ju4 xing2",
                    "definition": "sentence pattern (in grammar)",
                },
                {
                    "traditional": "句容",
                    "simplified": "句容",
                    "pinyin": "Ju4 rong2",
                    "definition": "Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu",  # noqa
                },
                {
                    "traditional": "句容市",
                    "simplified": "句容市",
                    "pinyin": "Ju4 rong2 shi4",
                    "definition": "Jurong county level city in Zhenjiang 鎮江|镇江[Zhen4 jiang1], Jiangsu",  # noqa
                },
                {
                    "traditional": "句式",
                    "simplified": "句式",
                    "pinyin": "ju4 shi4",
                    "definition": "sentence pattern/sentence structure/syntax",
                },
                {
                    "traditional": "句法",
                    "simplified": "句法",
                    "pinyin": "ju4 fa3",
                    "definition": "syntax",
                },
                {
                    "traditional": "句號",
                    "simplified": "句号",
                    "pinyin": "ju4 hao4",
                    "definition": "full stop/period (punct.)",
                },
                {
                    "traditional": "句點",
                    "simplified": "句点",
                    "pinyin": "ju4 dian3",
                    "definition": "period (punctuation)/(fig.) endpoint/finish",
                },
                {
                    "traditional": "名句",
                    "simplified": "名句",
                    "pinyin": "ming2 ju4",
                    "definition": "famous saying/celebrated phrase",
                },
                {
                    "traditional": "字句",
                    "simplified": "字句",
                    "pinyin": "zi4 ju4",
                    "definition": "words/expressions/writing",
                },
                {
                    "traditional": "字斟句酌",
                    "simplified": "字斟句酌",
                    "pinyin": "zi4 zhen1 ju4 zhuo2",
                    "definition": "weighing every word",
                },
                {
                    "traditional": "對句",
                    "simplified": "对句",
                    "pinyin": "dui4 ju2",
                    "definition": "couplet",
                },
                {
                    "traditional": "從句",
                    "simplified": "从句",
                    "pinyin": "cong2 ju4",
                    "definition": "clause",
                },
                {
                    "traditional": "感嘆句",
                    "simplified": "感叹句",
                    "pinyin": "gan3 tan4 ju4",
                    "definition": "exclamation/exclamatory phrase",
                },
                {
                    "traditional": "換句話說",
                    "simplified": "换句话说",
                    "pinyin": "huan4 ju4 hua4 shuo1",
                    "definition": "in other words",
                },
                {
                    "traditional": "斷句",
                    "simplified": "断句",
                    "pinyin": "duan4 ju4",
                    "definition": "to pause at appropriate points in reading aloud unpunctuated writing/to punctuate",  # noqa
                },
                {
                    "traditional": "樂句",
                    "simplified": "乐句",
                    "pinyin": "yue4 ju4",
                    "definition": "musical phrase",
                },
                {
                    "traditional": "疑問句",
                    "simplified": "疑问句",
                    "pinyin": "yi2 wen4 ju4",
                    "definition": "question (grammar)/interrogative sentence",
                },
                {
                    "traditional": "病句",
                    "simplified": "病句",
                    "pinyin": "bing4 ju4",
                    "definition": "defective sentence/error (of grammar or logic)",
                },
                {
                    "traditional": "短句",
                    "simplified": "短句",
                    "pinyin": "duan3 ju4",
                    "definition": "clause",
                },
                {
                    "traditional": "祈使句",
                    "simplified": "祈使句",
                    "pinyin": "qi2 shi3 ju4",
                    "definition": "imperative sentence",
                },
                {
                    "traditional": "絕句",
                    "simplified": "绝句",
                    "pinyin": "jue2 ju4",
                    "definition": "quatrain (poetic form)",
                },
                {
                    "traditional": "詞句",
                    "simplified": "词句",
                    "pinyin": "ci2 ju4",
                    "definition": "words and sentences",
                },
                {
                    "traditional": "詩句",
                    "simplified": "诗句",
                    "pinyin": "shi1 ju4",
                    "definition": "verse/CL:行[hang2]",
                },
                {
                    "traditional": "語句",
                    "simplified": "语句",
                    "pinyin": "yu3 ju4",
                    "definition": "sentence",
                },
                {
                    "traditional": "警句",
                    "simplified": "警句",
                    "pinyin": "jing3 ju4",
                    "definition": "aphorism",
                },
                {
                    "traditional": "造句",
                    "simplified": "造句",
                    "pinyin": "zao4 ju4",
                    "definition": "sentence-making",
                },
                {
                    "traditional": "陳述句",
                    "simplified": "陈述句",
                    "pinyin": "chen2 shu4 ju4",
                    "definition": "declarative sentence",
                },
                {
                    "traditional": "高句麗",
                    "simplified": "高句丽",
                    "pinyin": "Gao1 gou1 li2",
                    "definition": "Goguryeo (37 BC-668 AD), one of the Korean Three Kingdoms",  # noqa
                },
            ],
        }

        result = hanzi_dictionary.get_examples("橄")

        assert list(result.keys()) == freq_keys
        assert result == {
            "high_frequency": [
                {
                    "traditional": "橄欖",
                    "simplified": "橄榄",
                    "pinyin": "gan3 lan3",
                    "definition": "Chinese olive/olive",
                },
                {
                    "traditional": "橄欖油",
                    "simplified": "橄榄油",
                    "pinyin": "gan3 lan3 you2",
                    "definition": "olive oil",
                },
            ],
            "mid_frequency": [
                {
                    "traditional": "橄欖球",
                    "simplified": "橄榄球",
                    "pinyin": "gan3 lan3 qiu2",
                    "definition": "football played with oval-shaped ball (rugby, American football, Australian rules etc)",  # noqa
                },
                {
                    "traditional": "橄欖綠",
                    "simplified": "橄榄绿",
                    "pinyin": "gan3 lan3 lu:4",
                    "definition": "olive-green (color)",
                },
            ],
            "low_frequency": [
                {
                    "traditional": "橄欖枝",
                    "simplified": "橄榄枝",
                    "pinyin": "gan3 lan3 zhi1",
                    "definition": "olive branch/symbol of peace",
                },
                {
                    "traditional": "橄欖樹",
                    "simplified": "橄榄树",
                    "pinyin": "gan3 lan3 shu4",
                    "definition": "olive tree",
                },
                {
                    "traditional": "橄欖石",
                    "simplified": "橄榄石",
                    "pinyin": "gan3 lan3 shi2",
                    "definition": "olivine (rock-forming mineral magnesium-iron silicate (Mg,Fe)2SiO4)/peridot",  # noqa
                },
            ],
        }

    def test_determine_if_simplfied_char(self, hanzi_dictionary):
        simplified_char = hanzi_dictionary.determine_if_simplfied_char("句")
        traditional_char = hanzi_dictionary.determine_if_simplfied_char("學")

        assert simplified_char is True
        assert traditional_char is False

    def test_get_pinyin(self, hanzi_dictionary):
        result = hanzi_dictionary.get_pinyin("的")
        assert result == ["de5", "di1", "di2", "di4"]

        result = hanzi_dictionary.get_pinyin("句")
        assert result == ["gou1", "ju4"]

        result = hanzi_dictionary.get_pinyin("學")
        assert result == ["xue2"]

        result = hanzi_dictionary.get_pinyin("test")
        assert result is None

    def test_determine_phonetic_regularity(self, hanzi_dictionary):
        result = hanzi_dictionary.determine_phonetic_regularity("句")
        assert result == {
            "gou1": {
                "character": "句",
                "component": ["勹", "口", "勹", "口"],
                "phonetic_pinyin": ["bao1", "kou3", "bao1", "kou3"],
                "regularity": [0, 4, 0, 4],
            },
            "ju4": {
                "character": "句",
                "component": ["勹", "口", "勹", "口"],
                "phonetic_pinyin": ["bao1", "kou3", "bao1", "kou3"],
                "regularity": [0, 0, 0, 0],
            },
        }

        result = hanzi_dictionary.determine_phonetic_regularity("洋")
        assert result == {
            "yang2": {
                "character": "洋",
                "component": ["氵", "羊", "羊", "氵", "羊", "羊"],
                "phonetic_pinyin": [
                    "shui3",
                    "Yang2",
                    "yang2",
                    "shui3",
                    "Yang2",
                    "yang2",
                ],
                "regularity": [0, 1, 1, 0, 1, 1],
            }
        }

        # no result
        result = hanzi_dictionary.determine_phonetic_regularity("test")
        assert result is None

    def test_get_character_frequency(self, hanzi_dictionary):
        result = hanzi_dictionary.get_character_frequency("热")

        # CAREFUL: bound to change, dependent on entry data for cedict
        assert result == {
            "number": 606,
            "character": "热",
            "count": "67051",
            "percentage": "79.8453694124",
            "pinyin": "re4",
            "meaning": "heat/to heat up/fervent/hot (of weather)/warm up",
        }

        with pytest.raises(NotAHanziCharacter):
            result = hanzi_dictionary.get_character_frequency("test")

    def test_get_character_in_frequency_list_by_position(self, hanzi_dictionary):
        # CAREFUL: bound to change, dependent on entry data for char frequency
        result = hanzi_dictionary.get_character_in_frequency_list_by_position(111)
        assert result == {
            "number": 111,
            "character": "机",
            "count": "339823",
            "percentage": "43.7756134862",
            "pinyin": "ji1",
            "meaning": "machine/opportunity/secret",
        }

    def test_definition_lookup(self, hanzi_dictionary):
        result = hanzi_dictionary.definition_lookup("雪")

        assert result == [
            {
                "traditional": "雪",
                "simplified": "雪",
                "pinyin": "Xue3",
                "definition": "surname Xue",
            },
            {
                "traditional": "雪",
                "simplified": "雪",
                "pinyin": "xue3",
                "definition": "snow/CL:場|场[chang2]/(literary) to wipe away (a humiliation etc)",  # noqa
            },
        ]

        result = hanzi_dictionary.definition_lookup("這", "traditional")
        print(result)

        assert result == [
            {
                "traditional": "這",
                "simplified": "这",
                "pinyin": "zhe4",
                "definition": "this/these/(commonly pr. [zhei4] before a classifier, esp. in Beijing)",
            }
        ]

        # traditional but user asked simplified
        with pytest.raises(KeyError) as kerr:
            hanzi_dictionary.definition_lookup("這", "simplified")

        assert str(kerr.value) == "'這 not available in simplified dictionary.'"

        # no result
        with pytest.raises(NotAHanziCharacter):
            hanzi_dictionary.definition_lookup("test")
