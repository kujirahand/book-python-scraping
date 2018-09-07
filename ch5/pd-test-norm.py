import pandas as pd
# 身長・体重・タイプのデータフレームを生成
tbl = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2, 72.5 ],
    "height": [ 170,  180,  155,  143,  154,  160  ],
    "gender": [ "f",  "m",  "m",  "f",  "f",  "m"  ]
})

# 身長と体重を正規化
tbl["weight"] /= 100
tbl["height"] /= 200
print(tbl)

