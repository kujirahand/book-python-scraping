from sklearn import svm, metrics
import random, re

# アヤメのCSVデータを読み込む --- (※1)
lines = open('iris.csv', 'r', encoding='utf-8').read().split("\n")
f_tonum = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
f_cols  = lambda li: list(map(f_tonum,li.strip().split(',')))
csv = list(map(f_cols, lines))
del csv[0] # 先頭のヘッダ行を削除
random.shuffle(csv) # データをシャッフル

# データをK分割する --- (※2)
K = 5 
csvk = [ [] for i in range(K) ]
for i in range(len(csv)):
    csvk[i % K].append(csv[i])

# リストを訓練データとラベルに分割する関数
def split_data_label(rows):
    data = []; label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return (data, label)

# 正解率を求める --- (※3)
def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    # 区連データを学習して分類して正解率を求める
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)

# K分割したデータについて正解率を求める --- (※4)
score_list = []
for testc in csvk:
    # testc以外のデータを訓練データとする
    trainc = []
    for i in csvk:
        if i != testc: trainc += i
    sc = calc_score(testc, trainc)
    score_list.append(sc)
print("各正解率=", score_list)
print("平均正解率=", sum(score_list) / len(score_list))



