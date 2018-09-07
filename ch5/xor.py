import tensorflow as tf

# データを入れるプレースホルダを宣言
x = tf.placeholder(tf.float32, [None, 2], name="x")
# 変数を宣言
W = tf.Variable(tf.zeros([2, 2])); # 重み
b = tf.Variable(tf.zeros([2])); # バイアス
# ソフトマックス回帰
y = tf.nn.softmax(tf.matmul(x, W) + b)
# データの正解ラベルを入れるプレースホルダを宣言
y_ = tf.placeholder(tf.float32, [None, 2])
# モデルを訓練する
# 交差エントロピーを計算
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),
    reduction_indices=[1]))
# 交差エントリピーを最小化
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# セッションを開始
sess = tf.Session()
sess.run(tf.initialize_all_variables()) #変数を初期化
# テストデータを用いて学習させる
xor_pat = [[0,0],[0,1],[1,0],[1,1]]
xor_ans = [[1,0],[0,1],[0,1],[1,0]] # class [1,0]=>0 [0,1]=>1
for step in range(2000):
    e, a = sess.run(
        [cross_entropy, train_step], 
        feed_dict={x: xor_pat, y_:xor_ans})
    print("step:",step, "entropy:", e)

# データを予測
predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_,1))
acc = tf.reduce_mean(tf.cast(predict, "float"))
r = sess.run(acc, feed_dict={x: xor_pat, y_:xor_ans})
print(r)
