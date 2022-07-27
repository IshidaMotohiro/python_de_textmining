# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer

t = Tokenizer()

def tokens(text, pos = ['名詞', '形容詞', '動詞'], stopwords_list=[]):
    word_list = []
    for token in t.tokenize(text):
    ## 品詞が名詞なら
        tp = (token.part_of_speech).split(',')
        if token.base_form not in stopwords_list:
            if len(pos) < 1 or (tp[0] in pos):
                word_list.append(token.base_form)
    return word_list

if __name__ == '__main__':
    out = tokens("これは良い本です。")
    print(out)
