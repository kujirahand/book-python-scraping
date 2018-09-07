from gensim.models import word2vec

# 単語データを読み取り
data = word2vec.Text8Corpus('text/夏目漱石.wakati')
# データを元にモデルを構築
model = word2vec.Word2Vec(data, size=200)
# 類似語を表示する
cat_list = model.most_similar(positive="動物")
for w in cat_list:
    print(w[0], w[1])

