# ライブラリのインポート --- (※1)
import MySQLdb

# MySQLに接続する --- (※2)
conn = MySQLdb.connect(
    user='root',
    passwd='test-password',
    host='localhost',
    db='test')

# カーソルを取得する --- (※3)
cur = conn.cursor()

# テーブルを作成する --- (※4)
cur.execute('DROP TABLE IF EXISTS items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')

# データを挿入する --- (※5)
data = [('Banana', 300),('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s,%s)", i)

# データを抽出する --- (※6)
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

