from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils

image_w = 28
image_h = 28
nb_classes = 10

def main():
    # MNISTのデータを読む
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # データを正規化
    X_train = X_train.reshape(
        X_train.shape[0], image_w * image_h).astype('float32')
    X_test  = X_test.reshape(
        X_test.shape[0], image_w * image_h).astype('float32')
    X_train /= 255
    X_test  /= 255
    y_train = np_utils.to_categorical(y_train, 10)
    y_test  = np_utils.to_categorical(y_test, 10)
    # モデルを構築
    model = build_model()
    model.fit(X_train, y_train,
        batch_size=128, epochs=20, verbose=1,
        validation_data=(X_test, y_test))
    # モデルを保存
    model.save_weights('mnist.hdf5')
    # モデルを評価
    score = model.evaluate(X_test, y_test, verbose=0)
    print('score=', score)

def build_model():
    # MLPのモデルを構築
    model = Sequential()
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
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

