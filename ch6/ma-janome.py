from janome.tokenizer import Tokenizer
t = Tokenizer()
malist = t.tokenize("庭には二羽鶏がいる。")
for n in malist:
    print(n)
