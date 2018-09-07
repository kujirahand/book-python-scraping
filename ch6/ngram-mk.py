def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

a = "今日、渋谷で美味しいトンカツを食べた。"
b = "渋谷で食べた今日のトンカツは美味しかった。"

print(ngram(a, 2))
print(ngram(b, 2))


