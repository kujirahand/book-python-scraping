#!/usr/bin/env python3
import cgi, os.path
from sklearn.externals import joblib

# 学習データを読み込む
pklfile = os.path.dirname(__file__) + "/freq.pkl"
clf = joblib.load(pklfile)

# テキストの入力フォームを表示する
def show_form(text, msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
        <html><body><form>
        <textarea name="text" rows="8" cols="40">{0}</textarea>
        <p><input type="submit" value="判定"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(cgi.escape(text), msg))

# 判定する
def detect_lang(text):
    # アルファベットの出現頻度を調べる
    text = text.lower() 
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)]
    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n < 26: cnt[n] += 1
    total = sum(cnt)
    if total == 0: return "入力がありません"
    freq = list(map(lambda n: n/total, cnt))
    # 言語を予測する
    res = clf.predict([freq])
    # 言語コードを日本語に直す
    lang_dic = {"en":"英語","fr":"フランス語",
        "id":"インドネシア語", "tl":"タガログ語"}
    return lang_dic[res[0]]


# 投稿された値を読み取る
form = cgi.FieldStorage()
text = form.getvalue("text", default="")
msg = ""
if text != "":
    lang = detect_lang(text)
    msg = "判定結果:" + lang

# フォームを表示
show_form(text, msg)


