# IP確認APIへアクセスして結果を表示する

# モジュールを取り込む --- (※1)
import urllib.request

# データを取得する --- (※2)
url = "https://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# バイナリを文字列に変換 --- (※3)
text = data.decode("utf-8")
print(text)
