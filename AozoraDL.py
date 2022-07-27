
import re
import zipfile
import urllib.request
import os.path,glob
import sys
#ダウンロードしたいURLを入力する
# URL = 'https://www.aozora.gr.jp/cards/000081/files/43736_ruby_17601.zip'
args = sys.argv


URL = args[1]

if len(URL) == '':
    print('青空文庫のURLを入力してください')
    sys.exit()

def aozora(URL):
    download_text = download(URL)
    print(download_text)
    text = convert(download_text)
    # m = re.search('//(\\D+)', download_text)
    # print(m.group())
    m = re.findall('(\\w+.txt)', download_text)
    # print(m)
    print('ファイルの作成：' + m[0])
    f = open(m[0], mode='w', encoding='utf-8') # with open(download_text, mode='w', encoding='shift-jis') as f:
    f.write(text)    

def main():
    download_text = download(URL)
    print(download_text)
    text = convert(download_text)
    # m = re.search('//(\\D+)', download_text)
    # print(m.group())
    m = re.findall('(\\w+.txt)', download_text)
    # print(m)
    print('ファイルの作成：' + m[0])
    f = open(m[0], mode='w', encoding='utf-8') # with open(download_text, mode='w', encoding='shift-jis') as f:
    f.write(text)

def convert(download_text):
    binarydata = open(download_text, 'rb').read()
    text = binarydata.decode('shift_jis')

    # ルビ、注釈などの除去
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本：', text)[0]
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    text = text.strip()
    return text

def download(url):
 # データファイルをダウンロードする
    zip_file = re.split(r'/', url)[-1]
    if not os.path.exists(zip_file):
        print('Download URL')
        print('URL:',url)
        urllib.request.urlretrieve(url, zip_file)
    else:
        print('Download File exists')
        # フォルダの生成
    dir, ext = os.path.splitext(zip_file)
    if not os.path.exists(dir):
        os.makedirs(dir)
       # zipファイルの展開
    zip_obj = zipfile.ZipFile(zip_file, 'r')
    zip_obj.extractall(dir)
    zip_obj.close()
    # zipファイルの削除
    os.remove(zip_file)
    # テキストファイルの抽出
    path = os.path.join(dir,'*.txt')
    list = glob.glob(path)
    # print(list)
    return list[0]

if __name__ == "__main__":
    main()

