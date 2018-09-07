from sklearn import svm, metrics

# CSVファイルを読んで学習用データに整形 --- (※1)
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}

data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

# 学習 --- (※2)
clf = svm.SVC()
clf.fit(data["images"], data["labels"])

# 予測 --- (※3)
predict = clf.predict(test["images"])

# 結果がどの程度合っていたか確認 --- (※4)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("正解率=", ac_score)
print("レポート=")
print(cl_report)


