# ライブラリを取り込む --- (※1)
from bs4 import BeautifulSoup 

# 解析したいHTML --- (※2)
html = """
<html><body>
  <h1>スクレイピングとは？</h1>
  <p>Webページを解析すること。</p>
  <p>任意の箇所を抽出すること。</p>
</body></html>
"""

# HTMLを解析する --- (※3)
soup = BeautifulSoup(html, 'html.parser')

# 任意の部分を抽出する --- (※4)
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 要素のテキストを表示する --- (※5)
print("h1 = " + h1.string)
print("p  = " + p1.string)
print("p  = " + p2.string)


