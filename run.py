import csv
import codecs
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

# URLが記載されたファイルのパス
input_file_path = 'urls.txt'

# 現在の日付と時刻を取得
now = datetime.now()
now_str = now.strftime('%Y%m%d-%H%M')

# 結果を書き出すCSVファイルのパス。BOM付きUTF-8で書き出すためにcodecsを使う。
output_file_path = f'titlelist_{now_str}.csv'
output_file = codecs.open(output_file_path, 'w', 'utf-8-sig')

# URLのリストの読み込み
with open(input_file_path, 'r') as f:
    urls = [line.strip() for line in f]

# 各URLのページタイトルの取得
titles = []
for url in urls:
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        titles.append(soup.title.string)
    except Exception as e:
        print(f'エラーが発生しております🥺💦👉 {url}: {e}')
        titles.append('')

# 結果をCSVファイルに書き出し
writer = csv.writer(output_file)
for url, title in zip(urls, titles):
    writer.writerow([url, title])

# ファイルのクローズ
output_file.close()
