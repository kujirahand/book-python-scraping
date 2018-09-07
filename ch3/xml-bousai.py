from bs4 import BeautifulSoup 
import urllib.request as req
import os.path

# XMLをダウンロード --- (※1)
url = "http://www.city.yokohama.lg.jp/somu/org/kikikanri/data/shelter.xml"
savename = "shelter.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoupで解析 --- (※2)
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# データを各区ごとに確認 --- (※3)
info = {}
for i in soup.find_all("shelter"):
    name = i.find('name').string
    ward = i.find('ward').string
    addr = i.find('address').string
    note = i.find('notes').string
    if not (ward in info):
        info[ward] = []
    info[ward].append(name)

# 区ごとに防災拠点を表示
for ward in info.keys():
    print("+", ward)
    for name in info[ward]:
        print("| - ", name)

