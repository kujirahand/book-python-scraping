from bs4 import BeautifulSoup 

html = """
<html><body>
  <h1 id="title">スクレイピングとは？</h1>
  <p id="body">Webページから任意のデータを抽出すること</p>
</body></html>
"""

# HTMLを解析する --- (※1)
soup = BeautifulSoup(html, 'html.parser')

# find()メソッドで取り出す --- (※2)
title = soup.find(id="title")
body  = soup.find(id="body")

# テキスト部分を表示 
print("#title=" + title.string)
print("#body="  + body.string)

