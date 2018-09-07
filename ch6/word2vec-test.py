from gensim.models import word2vec

persons = ['夏目漱石', '太宰治', '芥川龍之介']
for person in persons:
    model = word2vec.Word2Vec.load('text/'+person+'.model')
    print("[", person, "の場合]")
    for word in ['結婚', '恋', '妻','人生']:
        words = model.most_similar(positive=[word])
        n = [w[0] for w in words]
        print(word,"=", ",".join(n))

