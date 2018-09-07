# ライブラリの取り込み --- (※1)
from bs4 import BeautifulSoup

# 解析対象となるHTMLを読み込む --- (※2)
html = open("eki-link.html", encoding="utf-8").read()

# HTMLを解析する --- (※3)
soup = BeautifulSoup(html, "html.parser")

# <a>タグを抽出する --- (※4)
links = soup.select("a[href]")

# (タイトル, URL)のリストを作る --- (※5)
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))

print(result)

