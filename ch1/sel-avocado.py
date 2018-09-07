from bs4 import BeautifulSoup 
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# CSSセレクタで選び出す
print(soup.select_one("li:nth-of-type(8)").string) #(1)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string) #(2)
print(soup.select("#ve-list > li[data-lo='us']")[1].string) #(3)
print(soup.select("#ve-list > li.black")[1].string) #(4)

# findメソッドで選び出す ---- (5)
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)

# findメソッドを二度組み合わせる --- (6)
print(soup.find(id="ve-list")
          .find("li", cond).string) 

