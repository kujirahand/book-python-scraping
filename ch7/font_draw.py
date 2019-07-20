import os, glob
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2, random

# サイズの指定
image_size = 28 # MNISTと同じサイズ

# フォントの列挙
ttf_list = glob.glob("/Library/Fonts/*.ttf") # Mac
ttf_list += glob.glob("~/Library/Fonts/*.ttf") # Mac
ttf_list += glob.glob("/usr/share/fonts/*.ttf") # Ubuntu
ttf_list += glob.glob("~/.fonts/*.ttf") # Ubuntu
print("font count=", len(ttf_list))

# 中央に文字を描画
def draw_text(im, font, text):
    dr = ImageDraw.Draw(im)
    im_sz = np.array(im.size)
    fo_sz = np.array(font.getsize(text))
    xy = (im_sz - fo_sz) / 2
    # print(im_sz, fo_sz)
    dr.text(xy, text, font=font, fill=(255))

# サンプル画像を出力するフォルダ
if not os.path.exists("./image/num"): os.makedirs("./image/num")

# 回転させたり拡大したりしてデータを水増しする
def gen_image(base_im, no, font_name):
    for ang in range(-20, 20, 2):
        sub_im = base_im.rotate(ang)
        data = np.asarray(sub_im)
        X.append(data)
        Y.append(no)
        w = image_size
        # 少しずつ拡大する
        for r in range(8, 15, 3):
            size = round((r/10) * image_size)
            im2 = cv2.resize(data, (size, size), cv2.INTER_AREA)
            data2 = np.asarray(im2)
            if image_size > size:
                x = (image_size - size) // 2
                data = np.zeros((image_size, image_size))
                data[x:x+size, x:x+size] = data2
            else:
                x = (size - image_size) // 2
                data = data2[x:x+w, x:x+w]
            X.append(data)
            Y.append(no)
            if random.randint(0, 400) == 0:
                fname = "image/num/n-{0}-{1}-{2}.png".format(
                    font_name, no, ang, r)
                cv2.imwrite(fname, data)



# 画像に描画
X = []
Y = []
for path in ttf_list:
    font_name = os.path.basename(path)
    try:
        fo = ImageFont.truetype(path, size=100)
    except:
        continue
    for no in range(10):
        im = Image.new("L", (200, 200))
        draw_text(im, fo, str(no))
        # フォントの描画範囲を得る
        ima = np.asarray(im)
        blur = cv2.GaussianBlur(ima, (5, 5), 0) # ぼかす
        th = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2) # 二値化
        contours = cv2.findContours(th, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if w < 10 or h < 10: continue
            num = ima[y:y+h, x:x+w] # 部分画像を得る
            ww = w if w > h else h
            wx = (ww - w) // 2
            wy = (ww - h) // 2
            spc = np.zeros((ww, ww))
            spc[wy:wy+h, wx:wx+w] = num # 中央にコピー
            num = cv2.resize(spc, (image_size, image_size), cv2.INTER_AREA)
            # 標準の形状をデータに追加
            X.append(num)
            Y.append(no)
            # 少しずつ回転する
            base_im = Image.fromarray(np.uint8(num))
            gen_image(base_im, no, font_name)

X = np.array(X)
Y = np.array(Y)
np.savez("./image/font_draw.npz", x=X, y=Y)
print("ok,", len(Y))


