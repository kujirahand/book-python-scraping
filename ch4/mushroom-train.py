import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# データの読み込み --- (※1)
mr = pd.read_csv("mushroom.csv", header=None)

# データ中の記号を数値に変換する --- (※2)
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.loc[0])
    row_data = []
    for v in row.loc[1:]:
        row_data.append(ord(v))
    data.append(row_data)

# 学習用とテスト用データに分ける --- (※3)
data_train, data_test, label_train, label_test = \
    train_test_split(data, label)

# データの学習 --- (※4)
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# データを予測 --- (※5)
predict = clf.predict(data_test)

# 合っているか結果を確認 --- (※6)
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート=\n", cl_report)


