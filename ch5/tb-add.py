import tensorflow as tf

# 定数や変数を宣言 --- (*1)
a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(0, name="v")

# 計算を行うグラフを定義 --- (*2)
calc_op = a + b * c 
assign_op = tf.assign(v, calc_op)

# セッションを生成 --- (*3)
sess = tf.Session()

# TensorBoardを使う --- (*4)
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# セッションを実行する --- (*5)
sess.run(assign_op)
print(sess.run(v))


