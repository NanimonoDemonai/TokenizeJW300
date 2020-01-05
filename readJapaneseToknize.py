from tqdm import tqdm
import json
from JapaneseTokenizer import JapaneseTokenizer

my_tokenizer = JapaneseTokenizer()

if __name__ == "__main__":

    num_lines = sum(1 for line in open("./mod/ja.txt", "r"))
    with open("./mod/ja.txt", "r") as f:
        with open("./tok/ja.txt", "w") as w:
            batch = []
            for line in tqdm(f, total=num_lines):
                batch.append(line)
                if len(batch) >= 1000:
                    res = my_tokenizer.tokenize(batch)
                    batch = []
                    for tokens, entities in res:
                        w.write(
                            " ".join(tokens) + '\t' + json.dumps(entities, ensure_ascii=False) + '\n')
            my_tokenizer.tokenize(batch)
            batch = []
