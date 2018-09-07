def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
	a = ngram(sa, num)
	b = ngram(sb, num)
	r = []
	cnt = 0
	for i in a:
		for j in b:
			if i == j:
				cnt += 1
				r.append(i)
	return cnt / len(a), r


a = "機械学習はとても面白い技術だから勉強しよう。"
b = "勉強すると面白い技術、機械学習を学ぼう。"
r2, word2 = diff_ngram(a, b, 2)
print(a,"\n",b)
print(r2, word2)

a = "本文とは関係なくマシュマロは美味しい。"
b = "マシュマロは本文とは関係なく美味しい。"
r2, word2 = diff_ngram(a, b, 2)
print(a,"\n",b)
print(r2, word2)

a = "Pythonのポイントはインデントによるブロック表現です。"
b = "しっかり水分補給すればインターハイでも優勝です。"
r2, word2 = diff_ngram(a, b, 2)
print(a,"\n",b)
print(r2, word2)

