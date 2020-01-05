import itertools

import spacy


class JapaneseTokenizer:
    nlp = spacy.load("ja_ginza", disable=["JapaneseCorrector"])

    def __init__(self):
        self._rids = []  # 捨てた単語置き場

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
    def _flatten(arr):
        """
        配列をflatにする
        [[A],[B]]->[A,B]
        """
        return itertools.chain.from_iterable(arr)

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
            for token in JapaneseTokenizer._flatten(doc.sents)  # flattenしてから送る
        ]

    @staticmethod
    def _entity(doc):
        return [
            (ent.text, ent.label_) for ent in doc.ents
        ]

    @staticmethod
    def _tokens_filter(tokens, callback):
        target = ""

        def window(token):
            nonlocal target
            ent = token[4]
            if ent != "":
                if ent == "LOC":
                    # 場所だけは残す
                    target = ""
                    return True
                if target == "":
                    target = ent
                    return True
                else:
                    if target == ent:
                        return False
                    else:
                        target = ent
                        return True
            target = ""
            return True

        return [callback(token) for token in tokens if window(token)]

    def _token_map_callback(self, token):
        # ent = token[4]
        if token[4] != "" and token[4] != "LOC":
            return "[" + token[4] + "]"
        # url = token[3]
        if token[3]:
            self._rids.append((token[0], "URL"))
            return "[URL]"
        # sym = token[2]
        if token[2]:
            self._rids.append((token[0], "SYM"))
            return "[SYM]"
        # num = token[1]
        if token[1]:
            self._rids.append((token[0], "NUM"))
            return "[NUM]"

        return token[0]

    def tokenize(self, s):
        self._rids = []
        doc = JapaneseTokenizer.nlp(s)
        tokens = JapaneseTokenizer._tokenize(doc)
        tokens = JapaneseTokenizer._tokens_filter(tokens, self._token_map_callback)
        entities = [*JapaneseTokenizer._entity(doc), *self._rids]
        return tokens, entities
