from janome.tokenizer import Tokenizer
import os, re, json, random

dict_file = "chatbot-data.json"
dic = {}
tokenizer = Tokenizer() # janome

# 辞書に単語を記録する --- (*1)
def register_dic(words):
    global dic
    if len(words) == 0: return
    tmp = ["@"]
    for i in words:
        word = i.surface
        if word == "" or word == "\r\n" or word == "\n": continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == "。" or word == "？":
            tmp = ["@"]
            continue
    # 辞書を更新するごとにファイルへ保存
    json.dump(dic, open(dict_file,"w", encoding="utf-8"))

# 三要素のリストを辞書として登録
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

# 作文する --- (*2)
def make_sentence(head):
    if not head in dic: return ""
    ret = []
    if head != "@": ret.append(head)        
    top = dic[head]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        if w1 in dic and w2 in dic[w1]:
            w3 = word_choice(dic[w1][w2])
        else:
            w3 = ""
        ret.append(w3)
        if w3 == "。" or w3 == "？" or w3 == "": break
        w1, w2 = w2, w3
    return "".join(ret)

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

# チャットボットに返答させる --- (*3)
def make_reply(text):
    # まず単語を学習する
    if text[-1] != "。": text += "。"
    words = tokenizer.tokenize(text)
    register_dic(words)
    # 辞書に単語があれば、そこから話す
    for w in words:
        face = w.surface
        ps = w.part_of_speech.split(',')[0]
        if ps == "感動詞":
            return face + "。"
        if ps == "名詞" or ps == "形容詞":
            if face in dic: return make_sentence(face)
    return make_sentence("@")

# 辞書があれば最初に読み込む
if os.path.exists(dict_file):
    dic = json.load(open(dict_file,"r"))


