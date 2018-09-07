from bs4 import BeautifulSoup 

# 解析対象となるHTML --- (※1)
html = """
<html><body>
<div id="meigen">
  <h1>トルストイの名言</h1>
  <ul class="items">
    <li>汝の心に教えよ、心に学ぶな</li>
    <li>謙虚な人は誰からも好かれる。</li>
    <li>強い人々は、いつも気取らない。</li>
  </ul>
</div>
</body></html>
"""

# HTMLを解析する --- (※2)
soup = BeautifulSoup(html, 'html.parser')

# 必要な部分をCSSクエリで取り出す
# | タイトル部分を取得 --- (※3)
h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)

# | リスト部分を取得 --- (※4)
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
	print("li =", li.string)


