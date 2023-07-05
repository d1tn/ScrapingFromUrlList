import csv
import codecs
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

# URLが記載されたファイルのパス
input_file_path = 'URLList.txt'

# 現在の日付と時刻を取得
now = datetime.now()
now_str = now.strftime('%Y%m%d-%H%M')

# 結果を書き出すCSVファイルのパス。BOM付きUTF-8で書き出すためにcodecsを使う。
output_file_path = f'list_{now_str}.csv'
output_file = codecs.open(output_file_path, 'w', 'utf-8-sig')

# URLのリストの読み込み
with open(input_file_path, 'r') as f:
    urls = [line.strip() for line in f]

# 各URLのページタイトル,descriptionの取得
titles = []
descriptions = []
for url in urls:
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        titles.append(soup.title.string)
        descriptions.append(soup.find('meta', attrs={'name':'description'})['content'] if soup.find('meta', attrs={'name':'description'}) else 'N/A')

    except Exception as e:
        print(f'エラーが発生しております🥺💦👉 {url}: {e}')
        descriptions.append('')


# 結果をCSVファイルに書き出し
writer = csv.writer(output_file)
for url, title, descriptions in zip(urls, titles, descriptions):
    writer.writerow([url, title, descriptions])

# ファイルのクローズ
output_file.close()
