import sys
import numpy as np
import cv2
import ocr_mnist

# フォントから生成した学習データを読む --- (※1)
mnist = ocr_mnist.build_model()
mnist.load_weights('font_draw.hdf5')

# 画像の読み込み --- (※2)
im = cv2.imread('numbers100.png')

# 輪郭を抽出 --- (※3)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # グレイスケールに
blur = cv2.GaussianBlur(gray, (5, 5), 0) # ぼかす
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2) # 二値化
cv2.imwrite("numbers100-th.png", thresh)
contours = cv2.findContours(thresh, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

# 抽出した座標を左上から右下へと並び替える --- (※4)
rects = []
im_w = im.shape[1]
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    if w < 10 or h < 10: continue # 小さすぎるのは飛ばす
    if w > im_w / 5: continue # 大きすぎるのも飛ばす
    y2 = round(y / 10) * 10 # Y座標を揃える
    index = y2 * im_w  + x
    rects.append((index, x, y, w, h))
rects = sorted(rects, key=lambda x:x[0]) # 並び替え

# 抽出した領域の画像データを得る --- (※5)
X = []
for i, r in enumerate(rects):
    index, x, y, w, h = r
    num = gray[y:y+h, x:x+w] # 部分画像を得る
    num = 255 - num # ネガポジ反転
    # 正方形の中に数字を描画
    ww = round((w if w > h else h) * 1.2) 
    spc = np.zeros((ww, ww))
    wy = (ww-h)//2
    wx = (ww-w)//2
    spc[wy:wy+h, wx:wx+w] = num
    num = cv2.resize(spc, (28, 28)) # MNISTのサイズに揃える
    # cv2.imwrite(str(i)+"-num.png", num) # 切り出した様子を保存
    # データを正規化
    num = num.reshape(28*28)
    num = num.astype("float32") / 255
    X.append(num)

# 切り出した画像を予測 --- (※6)
s = "31415926535897932384" + \
    "62643383279502884197" + \
    "16939937510582097494" + \
    "45923078164062862089" + \
    "98628034825342117067"
answer = list(s) 
ok = 0
nlist = mnist.predict(np.array(X))
for i, n in enumerate(nlist):
    ans = n.argmax()
    if ans == int(answer[i]):
        ok += 1
    else:
        print("[ng]", i, "字目", ans, "!=", answer[i], np.int32(n*100))

print("正解率:", ok / len(nlist))

