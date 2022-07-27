# -*- coding: utf-8 -*-

import spacy
nlp = spacy.load('ja_ginza_electra')
word_list=[]

def tokens(sentences, pos=['名詞', '形容詞', '動詞'], stopwords_list=[]):
    doc = nlp(sentences)
    for sent in doc.sents:
        for token in sent:
            i = (token.tag_.split('-'))[0]
            if i in pos:
                word_list.append(token.lemma_)
    return word_list

if __name__ == '__main__':
    out = tokens("今日の午後は八宝菜を食べました。")
    print(out)
