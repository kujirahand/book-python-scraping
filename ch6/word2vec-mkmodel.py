from gensim.models import word2vec

# 単語データからモデルを生成
persons = ['夏目漱石', '太宰治', '芥川龍之介']
for person in persons:
    print(person)
    data = word2vec.LineSentence('text/'+person+'.wakati')
    model = word2vec.Word2Vec(data, size=100,
        window=3, hs=1, min_count=1, sg=1)
    model.save('text/'+person+'.model')
print("ok")



