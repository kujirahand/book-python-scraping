# ファイル名とデータ
filename = "a.bin"
data = 100
# 書き込み
with open(filename, "wb") as f:
    f.write(bytearray([data]))
