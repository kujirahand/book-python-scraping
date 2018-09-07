import openpyxl 

# Excelファイルを開く --- (※1)
filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

# 先頭のシートを得る --- (※2)
sheet = book.worksheets[0]

# シートの各行を順に得る --- (※3)
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[2].value
    ])

# 先頭行は説明なので捨てる
del data[0]

# データを人口順に並び替える
data = sorted(data, key=lambda x:x[1])

# ワースト5を表示
for i, a in enumerate(data):
    if (i >= 5): break
    print(i+1, a[0], int(a[1]))

