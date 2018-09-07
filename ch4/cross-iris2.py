import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

# アヤメのCSVデータを読み込む --- (※1)
csv = pd.read_csv('iris.csv')

# リストを訓練データとラベルに分割する --- (※2)
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

# クロスバリデーションを行う --- (※3)
clf = svm.SVC()
scores = model_selection.cross_val_score(
	clf, data, label, cv=5)
print("各正解率=", scores)
print("正解率=", scores.mean())
