import sys
import numpy as np
import cv2

# 画像の読み込み
im = cv2.imread('numbers100.png')
# グレイスケールに変換しぼかした上で二値化する 
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

# 輪郭を抽出 --- (※1)
contours = cv2.findContours(
    thresh,      
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)[1]

# 抽出した領域を繰り返し処理する 
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt) # --- (※5)
    if h < 10: continue # 小さすぎるのは飛ばす
    cv2.rectangle(im, (x, y), (x+w, y+h), (0,0,255), 2)
cv2.imwrite('numbers100-cnt2.png', im)

