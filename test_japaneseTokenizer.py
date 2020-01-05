from pprint import pprint
from unittest import TestCase
import spacy

from normlizer import japanese_normalize
from tokenizer import JapaneseTokenizer

nlp = spacy.load("ja_ginza", disable=["JapaneseCorrector"])
test_str = "その ​ 後 ， 国 ​ が ​ 立て ​ た ​ 捕食 ​ 動物 ​ 抑制 ​ 計画 ​ に ​ より ， 1955 ​ 年 ​ から ​ 1964 ​ 年 ​ の ​ 間 ​ に ​ さらに ​ 2 万 7,646 ​ 匹 ​ の ​ コヨテ ​ が ​ 殺さ ​ れ ​ まし ​ た。"


class TestJapaneseTokenizer(TestCase):
    def test__tokenize(self):
        str = japanese_normalize(test_str)
        tokens = JapaneseTokenizer._tokenize(nlp(str))
        self.assertEqual(
            tokens,
            [
                (0, "その", False, False, ""),
                (1, "後", False, False, ""),
                (2, ",", False, False, ""),
                (3, "国", False, False, ""),
                (4, "が", False, False, ""),
                (5, "立て", False, False, ""),
                (6, "た", False, False, ""),
                (7, "捕食", False, False, ""),
                (8, "動物", False, False, ""),
                (9, "抑制", False, False, ""),
                (10, "計画", False, False, ""),
                (11, "に", False, False, ""),
                (12, "より", False, False, ""),
                (13, ",", False, False, ""),
                (14, "1955", True, False, "DATE"),
                (15, "年", False, False, "DATE"),
                (16, "から", False, False, ""),
                (17, "1964", True, False, "DATE"),
                (18, "年", False, False, "DATE"),
                (19, "の", False, False, ""),
                (20, "間", False, False, ""),
                (21, "に", False, False, ""),
                (22, "さらに", False, False, ""),
                (23, "2万7,646", False, False, ""),
                (24, "匹", False, False, ""),
                (25, "の", False, False, ""),
                (26, "コヨテ", False, False, ""),
                (27, "が", False, False, ""),
                (28, "殺さ", False, False, ""),
                (29, "れ", False, False, ""),
                (30, "まし", False, False, ""),
                (31, "た", False, False, ""),
                (32, "。", False, False, ""),
            ],
        )
