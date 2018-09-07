import openpyxl 

# Excelファイルを開く --- (※1)
filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

# アクティブになっているシートを得る --- (※2)
sheet = book.active

# 人口のトータルを計算する --- (※3)
total = 0
for i, row in enumerate(sheet.rows):
    if i == 0: continue # 先頭はヘッダ
    po = int(row[2].value)
    total += po
print("total=", total)

# 書き込む --- (※4)
sheet['A49'] = "Total"
sheet['C49'] = total

# フォントなどの設定を変更する --- (※5)
c = sheet['C49']
c.font = openpyxl.styles.Font(size=14, color="FF0000")
c.number_format = sheet['C48'].number_format

# 書き込んだ内容をファイルへ保存 --- (※6)
filename = "population-total.xlsx"
book.save(filename)
print("ok")

