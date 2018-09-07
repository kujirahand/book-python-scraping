from bs4 import BeautifulSoup 
fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# CSSセレクタで検索する方法
sel = lambda q : print(soup.select_one(q).string)
sel("#nu")               #(1)
sel("li#nu")             #(2)
sel("ul > li#nu")        #(3)
sel("#bible #nu")        #(4)
sel("#bible > #nu")      #(5)
sel("ul#bible > li#nu")  #(6)
sel("li[id='nu']")       #(7)
sel("li:nth-of-type(4)") #(8)

# その他の方法 
print(soup.select("li")[3].string)   #(9)
print(soup.find_all("li")[3].string) #(10)


