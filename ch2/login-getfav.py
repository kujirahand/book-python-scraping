# 作詞掲示板にログインしてお気に入りの詞を取得する
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ユーザー名とパスワードの指定 --- (※1)
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

# セッションを開始 --- (※2)
session = requests.session()

# ログイン --- (※3)
login_info = {
    "username_mmlbbs6": USER,  # ユーザー名を指定
    "password_mmlbbs6": PASS,  # パスワードを指定
    "back": "index.php",       # ログイン時に指定する値
    "mml_id": "0"              # ログイン時に指定する値
}
url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

# マイページのURLをピックアップする --- (※4)
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select_one(".islogin a")
if a is None:
    print("マイページが取得できませんでした")
    quit()
# 相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"]) 
print("マイページ=", url_mypage)

# マイページにアクセス --- (※5)
res = session.get(url_mypage)
res.raise_for_status()

# お気に入りの詞のタイトルを列挙 --- (※6)
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = a.attrs["href"]
    title = a.get_text()
    print("-", title, ">", href)



