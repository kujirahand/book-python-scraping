from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam 
from keras.utils import np_utils

# MNISTのデータを読み込む --- (※1)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# データをfloat32型に変換して正規化する --- (※2)
X_train = X_train.reshape(60000, 784).astype('float32')
X_test  = X_test.reshape(10000, 784).astype('float32')
X_train /= 255
X_test  /= 255
# ラベルデータを0-9までのカテゴリを表す配列に変換 --- (*2a)
y_train = np_utils.to_categorical(y_train, 10)
y_test  = np_utils.to_categorical(y_test, 10)

# モデルの構造を定義 --- (※3)
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation('softmax'))

# モデルを構築 --- (※4)
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(),
    metrics=['accuracy'])


# データで訓練 --- (※5)
hist = model.fit(X_train, y_train)

# テストデータを用いて評価する --- (※6)
score = model.evaluate(X_test, y_test, verbose=1)
print('loss=', score[0])
print('accuracy=', score[1])


