from pprint import pprint
from unittest import TestCase

from normlizer import japanese_normalize

test_str = "その ​ 後 ， 国 ​ が ​ 立て ​ た ​ 捕食 ​ 動物 ​ 抑制 ​ 計画 ​ に ​ より ， 1955 ​ 年 ​ から ​ 1964 ​ 年 ​ の ​ 間 ​ に ​ さらに ​ 2 万 7,646 ​ 匹 ​ の ​ コヨテ ​ が ​ 殺さ ​ れ ​ まし ​ た。"
test_str2 = "その ​ 後 、 国 ​ が ​ 立て ​ た ​ 捕食 ​ 動物 ​ 抑制 ​ 計画 ​ に ​ より 、 1955 ​ 年 ​ から ​ 1964 ​ 年 ​ の ​ 間 ​ に ​ さらに ​ 2 万 7,646 ​ 匹 ​ の ​ コヨテ ​ が ​ 殺さ ​ れ ​ まし ​ た。"


class TestJapanese_normalize(TestCase):
    def test_japanese_normalize(self):
        str = japanese_normalize(test_str)
        self.assertEqual(
            str, "その後,国が立てた捕食動物抑制計画により,1955年から1964年の間にさらに2万7,646匹のコヨテが殺されました。"
        )

    def test_japanese_normalize2(self):
        str = japanese_normalize(test_str2)
        self.assertEqual(
            str, "その後,国が立てた捕食動物抑制計画により,1955年から1964年の間にさらに2万7,646匹のコヨテが殺されました。"
        )
