import itertools

import spacy


class JapaneseTokenizer:
    nlp = spacy.load("ja_ginza", disable=["JapaneseCorrector"])

    @staticmethod
    def _tokenize(doc):
        return [
            (token.i, token.orth_, token.like_num, token.like_url, token.ent_type_)
            for token in itertools.chain.from_iterable(doc.sents)  # flattenしてから送る
        ]

    @staticmethod
    def _entity(doc):
        return [
            (ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents
        ]
