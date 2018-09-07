import os, re
from janome.tokenizer import Tokenizer

# 形態素解析 --- (※1)
def tokenize(text):
    t = Tokenizer()
    # テキストの先頭にあるヘッダとフッタを削除
    text = re.split(r'\-{5,}',text)[2]
    text = re.split(r'底本：', text)[0]
    text = text.strip()
    # ルビを削除
    text = text.replace('｜', '')
    text = re.sub(r'《.+?》', '', text)
    # テキスト内の脚注を削除
    text = re.sub(r'［＃.+?］', '', text)
    # 一行ずつ処理
    lines = text.split("\r\n")
    results = []
    for line in lines:
        res = []
        tokens = t.tokenize(line)
        for tok in tokens:
            bf = tok.base_form # 基本系
            if bf == "*": bf = tok.surface
            ps = tok.part_of_speech # 品詞情報
            hinsi = ps.split(',')[0]
            if hinsi in ['名詞', '動詞', '形容詞', '記号']:
                res.append(bf)
        l = " ".join(res)
        results.append(l)
    return results

# 辞書データの作成 --- (※2)
persons = ['夏目漱石', '太宰治', '芥川龍之介']
sakuhin_count = {}
for person in persons:
    person_dir = "./text/" + person
    sakuhin_count[person] = 0 # 作品数を数えるため
    results = []
    for sakuhin in os.listdir(person_dir):
        print(person, sakuhin) # 経過を表示するため
        sakuhin_count[person] += 1
        sakuhin_file = person_dir + "/" + sakuhin
        try:
            # 青空文庫のShift_JISファイルを読み込む
            bindata = open(sakuhin_file, "rb").read()
            text = bindata.decode("shift_jis")
            lines = tokenize(text) # 形態素解析
            results += lines
        except Exception as e:
            print("[error]", sakuhin_file, e)
            continue
    # ファイルへ保存 --- (※3)
    fname = "./text/" + person + ".wakati"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(person)         

print("作品数:", sakuhin_count)

