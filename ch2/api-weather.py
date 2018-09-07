import requests
import json, pprint

# APIキーの指定 - 以下を書き換えてください★ --- (※1)
apikey = "474d59dd890c4108f62f192e0c6fce01"

# 天気を調べたい都市の一覧 --- (※2)
cities = ["Tokyo,JP", "London,UK", "New York,US"]
# APIのひな型 --- (※3)
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換(ケルビン→摂氏) --- (※4)
k2c = lambda k: k - 273.15

# 各都市の温度を取得する --- (※5)
for name in cities:
    # APIのURLを得る --- (※6)
    url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする --- (※7)
    data = json.loads(r.text)
    # 結果を画面に表示 --- (※8)
    print("+ 都市=", data["name"])
    print("| 天気=", data["weather"][0]["description"])
    print("| 最低気温=", k2c(data["main"]["temp_min"]))
    print("| 最高気温=", k2c(data["main"]["temp_max"]))
    print("| 湿度=", data["main"]["humidity"])
    print("| 気圧=", data["main"]["pressure"])
    print("| 風速度=", data["wind"]["speed"])
    print("")

