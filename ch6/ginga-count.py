from janome.tokenizer import Tokenizer
import zipfile
import os.path, urllib.request as req

# 銀河鉄道の夜のZIPファイルをダウンロード --- (※1)
url = "http://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
local = "456_ruby_145.zip"
if not os.path.exists(local):
    print("ZIPファイルをダウンロード")
    req.urlretrieve(url, local)

# ZIPファイル内のテキストファイルを読む --- (※2)
zf = zipfile.ZipFile(local, 'r') # zipファイルを読む
fp= zf.open('gingatetsudono_yoru.txt', 'r') # アーカイブ内のテキストを読む
bindata = fp.read()
txt = bindata.decode('shift_jis') # テキストがShift_JISなのでデコード

# 形態素解析オブジェクトの生成 --- (※3)
t = Tokenizer()

# テキストを一行ずつ処理 --- (※4)
word_dic = {}
lines = txt.split("\r\n")
for line in lines:
    malist = t.tokenize(line)
    for w in malist:
        word = w.surface
        ps = w.part_of_speech # 品詞
        if ps.find('名詞') < 0: continue # 名詞だけカウント --- (※5)
        if not word in word_dic:
            word_dic[word] = 0
        word_dic[word] += 1 # カウント

# よく使われる単語を表示 --- (※6)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word,cnt in keys[:50]:
    print("{0}({1}) ".format(word,cnt), end="")

