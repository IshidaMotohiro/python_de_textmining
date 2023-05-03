# python_de_textmining

- [動画](#動画)
- [本書の分析をRで実行する方法](#本書の分析をRで実行する方法)
- [変更履歴](#変更履歴)

## 『Pythonで学ぶテキストマイニング』

拙著『Rによるテキストマイニング入門』（森北出版 2017）で扱ったデータを、Pythonでも分析できるように構成し直し、さらに単語分散表現の使い方、最近の自然言語処理で主流の Transformers についても解説した入門書です。

- 出版社 ‏ : ‎ シーアンドアール研究所
- 発売日 ‏ : ‎ 2022/8/13
- ISBN-13 ‏ : ‎ 978-4863543935  https://www.amazon.co.jp/dp/486354393X/


なお、Windows で MeCab を利用する場合は 64bit UTF-8 辞書版が必要です。公式の 32 bit 版 MeCab をすでにインストールしている場合は必ずアンインストールしてから、64bit版をインストールし直してください。 https://github.com/ikegami-yukino/mecab/releases 


## 動画

解説動画を公開します。
 
- 第２章 Python 速習： Miniforgeのインストール（M1チップmacOS編）: https://youtu.be/pDubtRcuth8
- 第２章 Python 速習：Jupyterの起動と終了 （M1チップmacOS Miniforge編）: https://youtu.be/0-AETjou8zA
- 第２章 Python 速習：Jupyterの使い方 : https://youtu.be/Y9qMibaa3uo
- 第２章 Python 速習： Python 速習 : テキスト分析：https://youtu.be/ifq-gmQvbhg
- 第３章 MeCab： MeCabのインストール(macOS)： https://youtu.be/0ePI8a9kNUI
- 第９章 第１０章 歴代首相所信表明演説の読み込みと分析（安倍元総理の演説分析）： https://youtu.be/5DfMDSucfRk


[![MeCab_Install](http://img.youtube.com/vi/0ePI8a9kNUI/0.jpg)](https://www.youtube.com/watch?v=0ePI8a9kNUI)

## Mac における MeCab のインストール

本書の手順で MeCab を導入しても、`import MeCab` を実行したときに、ライブラリが見当たらないというエラーが生じることがあります。
この場合、いったん Python 用の mecab-python3 をアンインストールし、今度は手元のMacでビルドし直してみます。

```
pip uninstall  mecab-python3
pip install --no-binary :all: mecab-python3
```

改めて `import MeCab` を実行してみます。再度エラーが生じた場合は、Macにデフォルトでインストールされている"/usr/lib/libmecab.dylib" 
に誤って関連付けられている可能性があります。otool でエラーでライブラリの関連付けと 
`_MeCab.cpython-311-darwin.so` 
の場所を確認し、そして（本書の記載通りにインストールした場合に存在するはずの）
`/usr/local/lib/libmecab.2.dylib`
に、手作業で関連付けをやり直します。以下は筆者の環境で実行した例です。

```
## _MeCab.cpython-311-darwin.so の関連付けを確認し
otool -L /Users/ishida/.pyenv/versions/3.11.1/lib/python3.11/site-packages/MeCab/_MeCab.cpython-311-darwin.so
## 誤った関連付けを修正する
### 以下の例では、誤って "/usr/lib/libmecab.dylib" と設定されているので、/usr/local/lib/libmecab.2.dylib と修正する
install_name_tool -change "/usr/lib/libmecab.dylib" /usr/local/lib/libmecab.2.dylib /Users/ishida/.pyenv/versions/3.11.1/lib/python3.11/site-packages/MeCab/_MeCab.cpython-311-darwin.so
```


## 本書の分析をRで実行する方法

『Rによるテキストマイニング入門』
出版社：森北出版
ISBN: 978-4627848429
https://www.amazon.co.jp/dp/4627848420

『実践 R によるテキストマイニング:センチメント分析・単語分散表現・機械学習・Pythonラッパー』
出版社：森北出版
ISBN: 978-4627885110
https://www.amazon.co.jp/dp/4627885113/


## 変更履歴

- Chapter02
  emoji-2.0.0では UNICODE_EMOJI が削除され EMOJI_DATA を利用する
- Chapter07
  CountVectorizer とファイルジェネレーターの項で引数指定を修正
- Chapter09
  transformers で日本語モデルを読み込む処理を行うセルがノートブックから削除されていたので修正


