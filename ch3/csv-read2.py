import csv, codecs

# CSVファイルを開く
filename = "list-sjis.csv"
fp = codecs.open(filename, "r", "shift_jis")

# 一行ずつ読む
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])



