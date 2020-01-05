from tqdm import tqdm
import json

from EnglishTokenizer import EnglishTokenizer

my_tokenizer = EnglishTokenizer()

if __name__ == "__main__":

    num_lines = sum(1 for line in open("./raw/en.txt", "r"))
    with open("./raw/en.txt", "r") as f:
        with open("./tok/en.txt", "w") as w:
            batch = []
            for line in tqdm(f, total=num_lines):
                batch.append(line.strip())
                if len(batch) >= 1000:
                    res = my_tokenizer.tokenize(batch)
                    batch = []
                    for tokens, entities in res:
                        w.write(
                            " ".join(tokens) + '\t' + json.dumps(entities, ensure_ascii=False) + '\n')
            my_tokenizer.tokenize(batch)
            batch = []
