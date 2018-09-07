import math, sys
from janome.tokenizer import Tokenizer # 形態素解析用

class BayesianFilter:
    """ ベイジアンフィルタ """
    def __init__(self):
        self.words = set() # 出現した単語を全て記録
        self.word_dict = {} # カテゴリごとの単語出現回数を記録
        self.category_dict = {} # カテゴリの出現回数を記録

    # 形態素解析を行う --- (※1)
    def split(self, text):
        result = []
        t = Tokenizer()
        malist = t.tokenize(text)
        for w in malist:
            sf = w.surface   # 区切られた単語そのまま 
            bf = w.base_form # 単語の基本形
            if bf == '' or bf == "*": bf = sf
            result.append(bf)
        return result

    # 単語とカテゴリを数える処理 --- (※2)
    def inc_word(self, word, category):
        # 単語をカテゴリに追加
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)
    def inc_category(self, category):
        # カテゴリを加算する
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # テキストを学習する --- (※3)
    def fit(self, text, category):
        """ テキストの学習 """
        word_list = self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)

    # カテゴリにおける単語リストのスコアを計算する --- (※4)
    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    # テキストのカテゴリ分けを行う --- (※5)
    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize 
        words = self.split(text)
        score_list = []
        for category in self.category_dict.keys():
            score = self.score(words, category)
            score_list.append((category, score))
            if score > max_score:
                max_score = score
                best_category = category
        return best_category, score_list

    # カテゴリ内の単語出現数を得る
    def get_word_count(self, word, category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0

    # カテゴリ/総カテゴリを計算
    def category_prob(self, category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        return category_v / sum_categories
        
    # カテゴリ内の単語の出現率を計算 --- (※6)
    def word_prob(self, word, category):
        n = self.get_word_count(word, category) + 1 # ---(*6a)
        d = sum(self.word_dict[category].values()) + len(self.words)
        return n / d


