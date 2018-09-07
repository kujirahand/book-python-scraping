import matplotlib.pyplot as plt
import pandas as pd

# PandasでCSVファイルを読む
tbl = pd.read_csv("bmi.csv", index_col=2)

# 描画を開始する
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# サブプロット用 - 指定のラベルを任意の色で描画
def scatter(lbl, color, marker="o"):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"],b["height"], c=color, label=lbl, marker=marker)

scatter("fat",    "red")
scatter("normal", "white")
scatter("thin",   "purple")

ax.legend() 
plt.savefig("bmi-test2.png")
# plt.show()

