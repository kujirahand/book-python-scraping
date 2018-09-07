import pandas as pd

# Excelファイルを開く --- (※1)
filename = "population.xlsx" # ファイル名
sheet_name = "list-sjis.csv" # シート名
book = pd.read_excel(filename, sheet_name=sheet_name)

# データを人口順に表示 --- (※2)
book.sort_values(by="法定人口", ascending=False)
print(book)



