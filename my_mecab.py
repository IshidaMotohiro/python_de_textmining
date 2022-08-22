# -*- coding: utf-8 -*-


import MeCab

# path = '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd'
path = ''
tagger = MeCab.Tagger(path)

def tokens(text, pos = ['名詞', '形容詞', '動詞']):
    text = ''.join(text.split())
    node = tagger.parseToNode(text)
    word_list = []
    while node:
        # print(node.surface)
        if node.surface != '':
            elem = node.feature.split(',')
            term = elem[6] if elem[6] != '*' else node.surface
            # print(elem[0])
            if len(pos) < 1 or elem[0] in pos:
                # print(term)
                word_list.append(term)
        node = node.next
    return word_list

if __name__ == '__main__':
    out = tokens("今日の午後は八宝菜を食べました。")
    print(out)

