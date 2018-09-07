import tensorflow as tf

# データフローグラフを構築 --- (*1)
a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b

# セッションを生成 --- (*2)
sess = tf.Session()

# TensorBoardを使う --- (*3)
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# セッションを実行する --- (*4)
print(sess.run(mul_op))


