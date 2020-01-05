import itertools

import spacy


class JapaneseTokenizer:
    nlp = spacy.load("ja_ginza", disable=["JapaneseCorrector"])

    @staticmethod
    def _isNum(token):
        return token.pos_ == "NUM" or token.like_num

    @staticmethod
    def _isSym(token):
        return token.pos_ == "SYM"

    @staticmethod
    def _isURL(token):
        return token.like_url

    @staticmethod
    def _tokenize(doc):
        return [
            (
                token.orth_,
                JapaneseTokenizer._isNum(token),
                JapaneseTokenizer._isSym(token),
                JapaneseTokenizer._isURL(token),
                token.ent_type_,
            )
            for token in itertools.chain.from_iterable(doc.sents)  # flattenしてから送る
        ]

    @staticmethod
    def _entity(doc):
        return [
            (ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents
        ]
