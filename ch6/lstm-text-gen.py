from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

# 元となるテキストを読み込む
path = "./text/夏目漱石/吾輩は猫である.txt"
bindata = open(path, "rb").read()
text = bindata.decode("shift_jis")
print('コーパスの長さ:', len(text))

# 一文字ずつバラバラにして文字にIDを振る
chars = sorted(list(set(text)))
print('使われている文字の数:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars)) # 文字→ID
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID→文字

# テキストをmaxlen文字で区切って、その文の次に来る文字を記録する
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('学習する文の数:', len(sentences))

print('テキストをIDベクトルにします...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# モデルを構築する(LSTM)
print('モデルを構築します...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

# 選択候補となる配列から値を取り出す
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# 学習させて、テキストを生成する・・・を繰り返す
for iteration in range(1, 60):
    print()
    print('-' * 50)
    print('繰り返し=', iteration)
    model.fit(X, y, batch_size=128, nb_epoch=1) # 訓練
    # ランダムにテキストのシードを選ぶ
    start_index = random.randint(0, len(text) - maxlen - 1)
    # 多様性のパラメータごとに文を生成する
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('---多様性=', diversity)
        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('---シード="' + sentence + '"')
        sys.stdout.write(generated)
        # シードを元にテキストを自動で生成する
        for i in range(400):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
            # 次に来る文字を予測
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]
            # 既存の文に予測した一文字を足す
            generated += next_char
            sentence = sentence[1:] + next_char
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()

