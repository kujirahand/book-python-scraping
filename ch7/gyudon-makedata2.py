from PIL import Image
import os, glob
import numpy as np
import random, math

# 分類対象のカテゴリを選ぶ 
root_dir = "./image/"
categories = ["normal", "beni", "negi", "cheese"]
nb_classes = len(categories)
image_size = 50

# 画像データを読み込む --- (※1)
X = [] # 画像データ
Y = [] # ラベルデータ
def add_sample(cat, fname, is_train):
    img = Image.open(fname)
    img = img.convert("RGB") # カラーモードの変更
    img = img.resize((image_size, image_size)) # 画像サイズの変更
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)
    if not is_train: return
    # 角度を変えたデータを追加
    # 少しずつ回転する
    for ang in range(-20, 20, 5):
        img2 = img.rotate(ang)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)
        # img2.save("gyudon-"+str(ang)+".png")
        # 反転する
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)

def make_sample(files, is_train):
    global X, Y
    X = []; Y = []
    for cat, fname in files:
        add_sample(cat, fname, is_train)
    return np.array(X), np.array(Y)

# ディレクトリごとに分けられたファイルを収集する --- (※2)
allfiles = []
for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for f in files:
        allfiles.append((idx, f))

# シャッフルして学習データとテストデータに分ける --- (※3)
random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.6)
train = allfiles[0:th]
test  = allfiles[th:]
X_train, y_train = make_sample(train, True)
X_test, y_test = make_sample(test, False)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/gyudon2.npy", xy)
print("ok,", len(y_train))




