from pprint import pprint
from unittest import TestCase
import spacy

from normlizer import japanese_normalize
from JapaneseTokenizer import JapaneseTokenizer

nlp = spacy.load("ja_ginza", disable=["JapaneseCorrector"])
test_str = "その ​ 後 ， 国 ​ が ​ 立て ​ た ​ 捕食 ​ 動物 ​ 抑制 ​ 計画 ​ に ​ より ， 1955 ​ 年 ​ から ​ 1964 ​ 年 ​ の ​ 間 ​ に ​ さらに ​ 2 万 7,646 ​ 匹 ​ の ​ コヨテ ​ が ​ 殺さ ​ れ ​ まし ​ た。"
test_str2 = "一 ​ 時期 ， エルサレム ​ の ​ 近く ​ の ​ 古代 ​ の ​ トフェト ​ で ​ も ， 同様 ​ の ​ 儀式 ​ が ​ 行なわ ​ れ ​ て ​ い ​ まし ​ た。"
test_str3 = "また ， アトラス ​ 誌 ​ に ​ 掲載 ​ さ ​ れ ​ た ， 日本 ​ から ​ の ​ 報道 ​ は ， 日本 ​ の ​ 子供 ​ たち ​ が ​ テレビ ​ で「ほとんど ​ 際限なく ​ 流血 ​ と ​ 暴力 ​ を ​ 見せ ​ られ ​ て ​ いる」こと ​ を ​ 示し ​ て ​ い ​ ます。"
my_tokenizer = JapaneseTokenizer()


class TestJapaneseTokenizer(TestCase):
    def test__tokenize(self):
        str = japanese_normalize(test_str)
        tokens = JapaneseTokenizer._tokenize(nlp(str))
        self.assertEqual(
            tokens,
            [
                ("その", False, False, False, ""),
                ("後", False, False, False, ""),
                (",", False, False, False, ""),
                ("国", False, False, False, ""),
                ("が", False, False, False, ""),
                ("立て", False, False, False, ""),
                ("た", False, False, False, ""),
                ("捕食", False, False, False, ""),
                ("動物", False, False, False, ""),
                ("抑制", False, False, False, ""),
                ("計画", False, False, False, ""),
                ("に", False, False, False, ""),
                ("より", False, False, False, ""),
                (",", False, False, False, ""),
                ("1955", True, False, False, "DATE"),
                ("年", False, False, False, "DATE"),
                ("から", False, False, False, ""),
                ("1964", True, False, False, "DATE"),
                ("年", False, False, False, "DATE"),
                ("の", False, False, False, ""),
                ("間", False, False, False, ""),
                ("に", False, False, False, ""),
                ("さらに", False, False, False, ""),
                ("2万7,646", True, False, False, ""),  # 漢数字がしっかり数値として扱われるか確認する
                ("匹", False, False, False, ""),
                ("の", False, False, False, ""),
                ("コヨテ", False, False, False, ""),
                ("が", False, False, False, ""),
                ("殺さ", False, False, False, ""),
                ("れ", False, False, False, ""),
                ("まし", False, False, False, ""),
                ("た", False, False, False, ""),
                ("。", False, False, False, ""),
            ],
        )

    def test__entity(self):
        str = japanese_normalize(test_str)
        entities = JapaneseTokenizer._entity(nlp(str))
        self.assertEqual(
            entities, [("1955年",  "DATE"), ("1964年", "DATE")]
        )

    def test__entity2(self):
        str = japanese_normalize(test_str2)
        entities = JapaneseTokenizer._entity(nlp(str))

        self.assertEqual(entities, [("エルサレム", "LOC")])

    def test__tokens_filter(self):
        str = japanese_normalize(test_str)
        tokens = JapaneseTokenizer._tokenize(nlp(str))
        self.assertEqual(
            JapaneseTokenizer._tokens_filter(tokens, lambda token: token),
            [
                ("その", False, False, False, ""),
                ("後", False, False, False, ""),
                (",", False, False, False, ""),
                ("国", False, False, False, ""),
                ("が", False, False, False, ""),
                ("立て", False, False, False, ""),
                ("た", False, False, False, ""),
                ("捕食", False, False, False, ""),
                ("動物", False, False, False, ""),
                ("抑制", False, False, False, ""),
                ("計画", False, False, False, ""),
                ("に", False, False, False, ""),
                ("より", False, False, False, ""),
                (",", False, False, False, ""),
                ("1955", True, False, False, "DATE"),  # 減っている
                ("から", False, False, False, ""),
                ("1964", True, False, False, "DATE"),  # 減っている
                ("の", False, False, False, ""),
                ("間", False, False, False, ""),
                ("に", False, False, False, ""),
                ("さらに", False, False, False, ""),
                ("2万7,646", True, False, False, ""),
                ("匹", False, False, False, ""),
                ("の", False, False, False, ""),
                ("コヨテ", False, False, False, ""),
                ("が", False, False, False, ""),
                ("殺さ", False, False, False, ""),
                ("れ", False, False, False, ""),
                ("まし", False, False, False, ""),
                ("た", False, False, False, ""),
                ("。", False, False, False, ""),
            ],
        )

    def test__tokens_map(self):
        str = japanese_normalize(test_str)
        tokens = JapaneseTokenizer._tokenize(nlp(str))
        self.assertEqual(
            my_tokenizer._tokens_filter(
                tokens, my_tokenizer._token_map_callback
            ),
            [
                "その",
                "後",
                ",",
                "国",
                "が",
                "立て",
                "た",
                "捕食",
                "動物",
                "抑制",
                "計画",
                "に",
                "より",
                ",",
                "[DATE]",
                "から",
                "[DATE]",
                "の",
                "間",
                "に",
                "さらに",
                "[NUM]",
                "匹",
                "の",
                "コヨテ",
                "が",
                "殺さ",
                "れ",
                "まし",
                "た",
                "。",
            ],
        )

    def test__tokens_map2(self):
        str = japanese_normalize(test_str2)
        tokens = JapaneseTokenizer._tokenize(nlp(str))
        self.assertEqual(
            my_tokenizer._tokens_filter(
                tokens, my_tokenizer._token_map_callback
            ),
            [
                "一時期",
                ",",
                "エルサレム",
                "の",
                "近く",
                "の",
                "古代",
                "の",
                "トフェト",
                "で",
                "も",
                ",",
                "同様",
                "の",
                "儀式",
                "が",
                "行なわ",
                "れ",
                "て",
                "い",
                "まし",
                "た",
                "。",
            ],
        )

    def test__tokens_map3(self):
        str = japanese_normalize(test_str3)
        tokens = JapaneseTokenizer._tokenize(nlp(str))
        self.assertEqual(
            JapaneseTokenizer._tokens_filter(
                tokens, my_tokenizer._token_map_callback
            ),
            [
                "また",
                ",",
                "[ORG]",
                "誌",
                "に",
                "掲載",
                "さ",
                "れ",
                "た",
                ",",
                "日本",
                "から",
                "の",
                "報道",
                "は",
                ",",
                "日本",
                "の",
                "子供",
                "たち",
                "が",
                "テレビ",
                "で",
                "「",
                "ほとんど",
                "際限",
                "なく",
                "流血",
                "と",
                "暴力",
                "を",
                "見せ",
                "られ",
                "て",
                "いる",
                "」",
                "こと",
                "を",
                "示し",
                "て",
                "い",
                "ます",
                "。",
            ],
        )

    def test_tokenize(self):
        s = japanese_normalize(test_str)
        tokens = my_tokenizer.tokenize(s)
        self.assertEqual(
            tokens,
            (
                [
                    "その",
                    "後",
                    ",",
                    "国",
                    "が",
                    "立て",
                    "た",
                    "捕食",
                    "動物",
                    "抑制",
                    "計画",
                    "に",
                    "より",
                    ",",
                    "[DATE]",
                    "から",
                    "[DATE]",
                    "の",
                    "間",
                    "に",
                    "さらに",
                    "[NUM]",
                    "匹",
                    "の",
                    "コヨテ",
                    "が",
                    "殺さ",
                    "れ",
                    "まし",
                    "た",
                    "。",
                ],
                [("1955年", "DATE"), ("1964年", "DATE"), ("2万7,646", "NUM")],
            ),
        )

    def test_tokenize3(self):
        s = japanese_normalize(test_str3)
        tokens = my_tokenizer.tokenize(s)
        self.assertEqual(
            tokens,
            (
                [
                    "また",
                    ",",
                    "[ORG]",
                    "誌",
                    "に",
                    "掲載",
                    "さ",
                    "れ",
                    "た",
                    ",",
                    "日本",
                    "から",
                    "の",
                    "報道",
                    "は",
                    ",",
                    "日本",
                    "の",
                    "子供",
                    "たち",
                    "が",
                    "テレビ",
                    "で",
                    "「",
                    "ほとんど",
                    "際限",
                    "なく",
                    "流血",
                    "と",
                    "暴力",
                    "を",
                    "見せ",
                    "られ",
                    "て",
                    "いる",
                    "」",
                    "こと",
                    "を",
                    "示し",
                    "て",
                    "い",
                    "ます",
                    "。",
                ],
                [("アトラス", "ORG"), ("日本", "LOC"), ("日本", "LOC")],
            ),
        )
