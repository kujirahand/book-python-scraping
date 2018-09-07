import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# アヤメのCSVデータを読み込む --- (※1)
csv = pd.read_csv('iris.csv')

# 任意の列を取り出す --- (※2)
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]

# 学習用とテスト用に分割する --- (※3)
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

# データを学習し、予測する --- (※4)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 正解率を求める --- (※5)
ac_score = metrics.accuracy_score(test_label, pre)
print("正解率=", ac_score)


