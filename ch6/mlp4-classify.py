from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout, Activation, Flatten
from keras.layers import Convolution1D, MaxPooling1D
from keras.layers import LSTM
from keras.optimizers import SGD
from keras.layers import Embedding

from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

from sklearn.cross_validation import train_test_split
from sklearn import cross_validation, metrics

import os,re,glob,json
import numpy as np
import pandas as pd

max_words = 67395 # 入力単語数
nb_classes = 9    # 9カテゴリを分類

batch_size = 32
nb_epoch = 5

max_features = 200
embedding_dims = 40 
nb_filter = 20
filter_length = 64
hidden_dims = 50

# CNNのモデルを生成
def build_model():
    model = Sequential()
    model.add(Embedding(max_features,
        embedding_dims,
        input_length=max_words,
        dropout=0.2))
    model.add(Convolution1D(
        nb_filter=nb_filter,
        filter_length=filter_length,
        border_mode='valid',
        activation='relu',
        subsample_length=1))
    model.add(MaxPooling1D(
        pool_length=model.output_shape[1]))
    model.add(Flatten())
    model.add(Dense(hidden_dims))
    model.add(Dropout(0.5))
    model.add(Activation('relu'))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    print(model.summary())
    return model

# モデルを生成
model = KerasClassifier(
    build_fn=build_model, 
    nb_epoch=nb_epoch, 
    batch_size=batch_size)

# テストデータを読み込み
data = json.load(open("./newstext/data-mini.json"))
X = data["X"]
Y = data["Y"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print(len(X_train),len(Y_train))

# 学習
model.fit(X_train, Y_train, verbose=1)

y = model.predict(X_test)
print(y)
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test, y)
print("正解率=", ac_score)
print("レポート=\n", cl_report)


