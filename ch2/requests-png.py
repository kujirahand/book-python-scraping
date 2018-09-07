# 画像データを取得
import requests
r = requests.get("https://uta.pw/shodou/img/3/3.png")

# バイナリ形式でデータを得て保存
with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")

