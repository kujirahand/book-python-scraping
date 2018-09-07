from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import json

nb_classes = 9    # 9カテゴリを分類

batch_size = 64 
nb_epoch = 20

# MLPのモデルを生成 --- (※1)
def build_model():
    global max_words
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    return model

# データを読み込み --- (※2)
data = json.load(open("./newstext/data-mini.json"))
# data = json.load(open("./newstext/data.json"))
X = np.array(data["X"]) # テキストを表すデータ
Y = np.array(data["Y"]) # カテゴリデータ
# 最大単語数を指定
max_words = len(X[0])

# 学習 --- (※3)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
print(len(X_train),len(Y_train))
Y_train = np_utils.to_categorical(Y_train, nb_classes)
model = KerasClassifier(
    build_fn=build_model, 
    epochs=nb_epoch, 
    batch_size=batch_size)
model.fit(X_train, Y_train)

# 予測 --- (※4)
y = model.predict(X_test)
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test, y)
print("正解率=", ac_score)
print("レポート=\n", cl_report)


