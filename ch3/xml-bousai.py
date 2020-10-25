from bs4 import BeautifulSoup 
import urllib.request as req
import os.path
import zipfile

# ZIPをダウンロード --- (※1)
url = "https://www.city.yokohama.lg.jp/kurashi/bousai-kyukyu-bohan/bousai-saigai/bosai/data/data.files/shelter.zip"
savezip = "shelter.zip"
savename = "shelter.xml"
if not os.path.exists(savezip):
    req.urlretrieve(url, savezip)
# ZIPを解凍
with zipfile.ZipFile(savezip, 'r')as zf:
    zf.extractall('./')

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

