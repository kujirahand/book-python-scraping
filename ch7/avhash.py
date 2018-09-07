from PIL import Image
import numpy as np

# 画像データをAverage Hashに変換 --- (※1)
def average_hash(fname, size = 16):
    img = Image.open(fname) # 画像データを開く--- (※2)
    img = img.convert('L') # グレースケールに変換 --- (※3)
    img = img.resize((size, size), Image.ANTIALIAS) # リサイズ --- (※4)
    pixel_data = img.getdata() # ピクセルデータを得る --- (※5)
    pixels = np.array(pixel_data) # Numpyの配列に変換 --- (※6)
    pixels = pixels.reshape((size, size)) # 二次元の配列に変換 --- (※7)
    avg = pixels.mean() # 算術平均を計算 --- (※8)
    diff = 1 * (pixels > avg) # 平均以上と以下で値を1と0に変換 --- (※9)
    return diff

# 二進数とみなしてハッシュ値に変換 --- (※10)
def np2hash(n):
    bhash = []
    for nl in ahash.tolist():
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2) # 二進数を整数に
        bhash.append("%04x" % i)
    return "".join(bhash)


# Average Hashを表示
ahash = average_hash('tower.jpg')
print(ahash)
print(np2hash(ahash))


