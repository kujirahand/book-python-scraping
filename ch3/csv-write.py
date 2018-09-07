import csv, codecs

with codecs.open("test.csv", "w", "shift_jis") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "商品名", "値段"])
    writer.writerow(["1000", "SDカード", 300])
    writer.writerow(["1001", "キーボード", 2100])
    writer.writerow(["1002", "マジック(赤,青)", 150])

