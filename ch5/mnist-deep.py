import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data 

# MINSTの手書き画像データを読み込む --- (*1)
mnist = input_data.read_data_sets("mnist/", one_hot=True)

pixels = 28 * 28 # 28x28ピクセル
nums = 10 # 0-9の10クラスに分ける

# プレースホルダを定義 --- (*2)
x  = tf.placeholder(tf.float32, shape=(None, pixels), name="x") # 画像データ
y_ = tf.placeholder(tf.float32, shape=(None, nums), name="y_")  # 正解ラベル 

# 重みとバイアスを初期化する関数 --- (*3)
def weight_variable(name, shape):
    W_init = tf.truncated_normal(shape, stddev=0.1)
    W = tf.Variable(W_init, name="W_"+name)
    return W
def bias_variable(name, size):
    b_init = tf.constant(0.1, shape=[size])
    b = tf.Variable(b_init, name="b_"+name)
    return b

# 畳み込みを行う関数 --- (*4)
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')
# 最大プーリングを行う関数 --- (*5)
def max_pool(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1],
        strides=[1,2,2,1], padding='SAME')

# 畳み込み層1 --- (*6)
with tf.name_scope('conv1') as scope:
    W_conv1 = weight_variable('conv1', [5, 5, 1, 32])
    b_conv1 = bias_variable('conv1', 32)
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

# プーリング層1 ---- (*7)
with tf.name_scope('pool1') as scope:
    h_pool1 = max_pool(h_conv1)

# 畳み込み層2 --- (*8)
with tf.name_scope('conv2') as scope:
    W_conv2 = weight_variable('conv2', [5, 5, 32, 64])
    b_conv2 = bias_variable('conv2', 64)
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

# プーリング層2 --- (*9)
with tf.name_scope('pool2') as scope:
    h_pool2 = max_pool(h_conv2)

# 全結合レイヤー --- (*10)
with tf.name_scope('fully_connected') as scope:
    n = 7 * 7 * 64
    W_fc = weight_variable('fc', [n, 1024])
    b_fc = bias_variable('fc', 1024)
    h_pool2_flat = tf.reshape(h_pool2, [-1, n])
    h_fc = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc) + b_fc)        

# ドロップアウト(過剰適合)を排除 --- (*11)
with tf.name_scope('dropout') as scope:
    keep_prob = tf.placeholder(tf.float32)
    h_fc_drop = tf.nn.dropout(h_fc, keep_prob)

# 読み出し層 --- (*12)
with tf.name_scope('readout') as scope:
    W_fc2 = weight_variable('fc2', [1024, 10])
    b_fc2 = bias_variable('fc2', 10)
    y_conv = tf.nn.softmax(tf.matmul(h_fc_drop, W_fc2) + b_fc2)

# モデルの学習 --- (*13)
with tf.name_scope('loss') as scope:
    cross_entoropy = -tf.reduce_sum(y_ * tf.log(y_conv))
with tf.name_scope('training') as scope:
    optimizer = tf.train.AdamOptimizer(1e-4)
    train_step = optimizer.minimize(cross_entoropy)

# モデルの評価 --- (*14)
with tf.name_scope('predict') as scope:
    predict_step = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy_step = tf.reduce_mean(tf.cast(predict_step, tf.float32))

# feed_dictの設定 --- (*15)
def set_feed(images, labels, prob):
    return {x: images, y_: labels, keep_prob: prob}

# セッションを開始 --- (*16)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # TensorBoardへの書き込み準備
    tw = tf.summary.FileWriter('log_dir', graph=sess.graph)
    # テスト用のフィードを生成
    test_fd = set_feed(mnist.test.images, mnist.test.labels, 1)
    # 訓練を開始 ---- (*17)
    for step in range(10000):
        batch = mnist.train.next_batch(50)
        fd = set_feed(batch[0], batch[1], 0.5)
        _, loss = sess.run([train_step, cross_entoropy], feed_dict=fd)
        if step % 100 == 0:
            acc = sess.run(accuracy_step, feed_dict=test_fd)
            print("step=", step, "loss=", loss, "acc=", acc)
    # 最終結果を表示
    acc = sess.run(accuracy_step, feed_dict=test_fd)
    print("正解率=", acc)




