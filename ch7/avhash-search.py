from PIL import Image
import numpy as np
import os, re

# ファイルパスの指定
search_dir = "./image/101_ObjectCategories"
cache_dir = "./image/cache_avhash"

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

# 画像データをAverage hashに変換 --- (※1)
def average_hash(fname, size = 16):
    fname2 = fname[len(search_dir):]
    # 画像をキャッシュしておく
    cache_file = cache_dir + "/" + fname2.replace('/', '_') + ".csv"
    if not os.path.exists(cache_file): # ハッシュを作成
        img = Image.open(fname)
        img = img.convert('L').resize((size, size), Image.ANTIALIAS)
        pixels = np.array(img.getdata()).reshape((size, size))
        avg = pixels.mean()
        px = 1 * (pixels > avg)
        np.savetxt(cache_file, px, fmt="%.0f", delimiter=",")
    else: # 既にキャッシュがあればファイルから読み込み
        px = np.loadtxt(cache_file, delimiter=",")
    return px

# 簡単にハミング距離を求める --- (※2)
def hamming_dist(a, b):
    aa = a.reshape(1, -1) # 1次元の配列に変換
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist

# 全てのディレクトリを列挙 --- (※3)
def enum_all_files(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(root, f)
            if re.search(r'\.(jpg|jpeg|png)$', fname):
                yield fname

# 画像を検索 --- (※4)
def find_image(fname, rate):
    src = average_hash(fname)
    for fname in enum_all_files(search_dir):
        dst = average_hash(fname)
        diff_r = hamming_dist(src, dst) / 256
        # print("[check] ",fname)
        if diff_r < rate:
            yield (diff_r, fname)

# 検索 --- (※5)
srcfile = search_dir + "/chair/image_0016.jpg"
html = ""
sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x:x[0])
for r, f in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[差異:' + str(r) + '-' + \
        os.path.basename(f) + ']</h3>'+ \
        '<p><a href="' + f + '"><img src="' + f + '" width=400>'+ \
        '</a></p></div>'
    html += s
# HTMLを出力
html = """<html><body><h3>元画像</h3><p>
<img src='{0}' width=400></p>{1}
</body></html>""".format(srcfile, html)
with open("./avhash-search-output.html", "w", encoding="utf-8") as f:
    f.write(html)
print("ok")


