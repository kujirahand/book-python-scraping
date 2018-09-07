from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import numpy as np

image_w = 28
image_h = 28
nb_classes = 10

def main():
    # フォント画像のデータを読む
    xy = np.load("./image/font_draw.npz")
    X = xy["x"]
    Y = xy["y"]
    # データを正規化
    X = X.reshape(X.shape[0], image_w * image_h).astype('float32')
    X /= 255
    Y = np_utils.to_categorical(Y, 10)
    # 訓練データとテストデータに分割
    X_train, X_test, y_train, y_test = \
        train_test_split(X, Y)
    # モデルを構築
    model = build_model()
    model.fit(X_train, y_train,
        batch_size=128, epochs=50, verbose=1,
        validation_data=(X_test, y_test))
    # モデルを保存
    model.save_weights('font_draw.hdf5')
    # モデルを評価
    score = model.evaluate(X_test, y_test, verbose=0)
    print('score=', score)

def build_model():
    # MLPのモデルを構築
    model = Sequential()
    model = Sequential()
    model.add(Dense(512, input_shape=(image_w * image_h,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
        optimizer=RMSprop(),
        metrics=['accuracy'])
    return model

if __name__ == '__main__':
    main()

