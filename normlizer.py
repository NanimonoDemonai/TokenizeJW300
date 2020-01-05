import neologdn


def japanese_normalize(str):
    return neologdn.normalize("".join(str.replace("\u200b", "").replace("、", ",").split()))
