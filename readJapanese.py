from tqdm import tqdm

from JapaneseTokenizer import JapaneseTokenizer
from normlizer import japanese_normalize

my_tokenizer = JapaneseTokenizer()

if __name__ == "__main__":

    num_lines = sum(1 for line in open("./raw/ja.txt", "r"))
    with open("./raw/ja.txt", "r") as f:
        with open("./mod/ja.txt", "w") as w:
            for line in tqdm(f, total=num_lines):
                w.write(japanese_normalize(line)+'\n')
