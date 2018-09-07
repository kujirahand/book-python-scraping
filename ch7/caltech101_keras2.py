from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense
import h5py
from PIL import Image
import numpy as np
import os


# カテゴリの指定
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)
# 画像サイズを指定
image_w = 64 
image_h = 64

# データをロード --- (※1)
X_train, X_test, y_train, y_test = np.load("./image/5obj.npy")
# データを正規化する
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)

# モデルを構築 --- (※2)
in_shape = X_train.shape[1:]
model = Sequential()
model.add(Conv2D(32, 3, input_shape=in_shape)) # ----(*2a)
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten()) # --- (※3) 
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes)) # ---- (*3a)
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

# モデルを訓練する --- (※4)
hdf5_file = "./image/5obj-model.hdf5"
if os.path.exists(hdf5_file):
    model.load_weights(hdf5_file)
else:
    model.fit(X_train, y_train, batch_size=32, epochs=50)
    model.save_weights(hdf5_file)

# モデルを評価する --- (※5)
pre = model.predict(X_test)
for i,v in enumerate(pre):
    pre_ans = v.argmax()
    ans = y_test[i].argmax()
    dat = X_test[i]
    if ans == pre_ans: continue
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    fname = "image/error/" + str(i) + "-" + categories[pre_ans] + \
        "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.uint8(dat))
    img.save(fname)


score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])


