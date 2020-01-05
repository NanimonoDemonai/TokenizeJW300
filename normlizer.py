import neologdn
import itertools


def japanese_normalize(str):
    neologdn.normalize("".join(str.replace("\u200b", "").split()))
