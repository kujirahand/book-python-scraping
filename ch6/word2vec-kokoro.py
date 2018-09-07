from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

# テキストファイルの読み込み --- (※1)
bindata = open('kokoro.txt.sjis', 'rb').read()
text = bindata.decode('shift_jis')

# テキストの先頭にあるヘッダとフッタを削除 --- (※2)
text = re.split(r'\-{5,}',text)[2]
text = re.split(r'底本：', text)[0]
text = text.strip()

# 形態素解析 --- (※3)
t = Tokenizer()
results = []
# テキストを一行ずつ処理する
lines = text.split("\r\n")
for line in lines:
    s = line
    s = s.replace('｜', '')
    s = re.sub(r'《.+?》', '', s) # ルビを削除
    s = re.sub(r'［＃.+?］', '', s) # 入力注を削除
    tokens = t.tokenize(s) # 形態素解析
    # 必要な語句だけを対象とする --- (※4)
    r = []
    for tok in tokens:
        if tok.base_form == "*": # 単語の基本系を採用
            w = tok.surface
        else:
            w = tok.base_form
        ps = tok.part_of_speech # 品詞情報
        hinsi = ps.split(',')[0]
        if hinsi in ['名詞', '形容詞', '動詞', '記号']:
            r.append(w)
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl) # --- 画面に分かち書きした行を表示

# 書き込み先テキストを開く --- (※5)
wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))

# Word2Vecでモデルを作成 --- (※6)
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, 
    size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok')



