# データを取得
import requests
r = requests.get("https://api.aoikujira.com/time/get.php")

# テキスト形式でデータを得る
text = r.text
print(text)

# バイナリ形式でデータを得る
bin = r.content
print(bin)

