import sqlite3

# データベースに接続 --- (※1)
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

# テーブルを作成 --- (※2)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items") 
cur.execute(""" CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name    TEXT,
    price   INTEGER)""")
conn.commit()

# 単発でデータを挿入 --- (※3)
cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name,price) VALUES (?,?)",
    ("Orange", 520))
conn.commit()

# 連続でデータを挿入 --- (※4)
cur = conn.cursor()
data = [("Mango",770), ("Kiwi",400), ("Grape",800),
    ("Peach",940),("Persimmon",700),("Banana", 400)]
cur.executemany(
    "INSERT INTO items(name,price) VALUES (?,?)",
    data)
conn.commit()

# 400-700円のデータを抽出して表示 --- (※5)
cur = conn.cursor()
price_range = (400, 700)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?",
    price_range)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)

