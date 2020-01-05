from unittest import TestCase

from EnglishTokenizer import EnglishTokenizer

test_str = "Thereafter a federal predator - control program brought death to an additional 27,646 red wolves between 1955 and 1964."
my_tokenizer = EnglishTokenizer()


class TestEnglishTokenizer(TestCase):
    def test_tokenize(self):
        tokens = my_tokenizer.tokenize(test_str)
        self.assertEqual(
            tokens,
            (
                [
                    "Thereafter",
                    "a",
                    "federal",
                    "predator",
                    "-",
                    "control",
                    "program",
                    "brought",
                    "death",
                    "to",
                    "an",
                    "additional",
                    "[NUM]",
                    "red",
                    "wolves",
                    "[DATE]",
                    ".",
                ],
                [
                    ("an additional 27,646", "CARDINAL"),
                    ("between 1955 and 1964", "DATE"),
                    ("27,646", "NUM"),
                ],
            ),
        )
