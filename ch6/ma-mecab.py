import MeCab
mecab = MeCab.Tagger("-Ochasen") # MeCabオブジェクトを生成
malist = mecab.parse("庭には二羽鶏がいる。") # 形態素解析を行う
print(malist)

