from janome.tokenizer import Tokenizer
import os, glob

# Janomeを使って形態素解析を行う
ja_tokenizer = Tokenizer()

# 日本語を分かち書き
def ja_tokenize(text):
    res = []
    lines = text.split("\n")
    lines = lines[2:] # 最初の二行はヘッダ情報なので捨てる
    for line in lines:
        malist = ja_tokenizer.tokenize(line)
        for tok in malist:
            ps = tok.part_of_speech.split(",")[0]
            if not ps in ['名詞','動詞','形容詞']: continue
            w = tok.base_form
            if w == "*" or w == "": w = tok.surface
            if w == "" or w == "\n": continue
            res.append(w)
        res.append("\n")
    return res

# テストデータを読み込み
root_dir = './newstext'
for path in glob.glob(root_dir+"/*/*.txt", recursive=True):
    if path.find("LICENSE") > 0: continue
    print(path)
    path_wakati = path + ".wakati"
    if os.path.exists(path_wakati): continue
    text = open(path, "r").read()
    words = ja_tokenize(text)
    wt = " ".join(words)
    open(path_wakati, "w", encoding="utf-8").write(wt)

