import urllib.request
import urllib.parse

API = "https://api.aoikujira.com/zip/xml/get.php"

# パラメータをURLエンコードする --- (※1)
values = {
    'fmt': 'xml',
    'zn': '1500042'
}
params = urllib.parse.urlencode(values)

# リクエスト用のURLを生成 --- (※2)
url = API + "?" + params
print("url=", url)

# ダウンロード --- (※3)
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
