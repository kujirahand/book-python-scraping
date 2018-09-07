import tensorflow as tf

# プレースホルダを定義 --- (※1)
a = tf.placeholder(tf.int32, [None]) # 整数型の配列サイズ指定なし

# 配列を10倍にする演算を定義 
b = tf.constant(10);
x10_op = a * b;

# セッションを開始 
sess = tf.Session()

# プレースホルダーに値を当てはめて実行 --- (※2)
r1 = sess.run(x10_op, feed_dict={a: [1,2,3,4,5]})
print(r1)
r2 = sess.run(x10_op, feed_dict={a: [10,20]})
print(r2)

