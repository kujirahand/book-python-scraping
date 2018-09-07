from bs4 import BeautifulSoup 
import re # 正規表現を使う時 --- (*1)

html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")
# 正規表現でhrefからhttpsのものを抽出 --- (*2)
li = soup.find_all(href=re.compile(r"^https://"))
for e in li: print(e.attrs['href'])


