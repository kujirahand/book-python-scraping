import numpy as np

# 10個のfloat32型の0データを生成
v = np.zeros(10, dtype=np.float32)
print(v)

# 連番で10個のuint64型のデータを生成
v = np.arange(10, dtype=np.uint64)
print(v)

# vの値を3倍にする
v *= 3
print(v)

# vの平均値を求める
print(v.mean())


