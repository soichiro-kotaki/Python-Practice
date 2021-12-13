from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd

"""
①解析したいサイトのurlを変数urlに代入
②requestモジュールのurlopenメソッドで、引数に指定したurlのサイトの全てのhtmlタグを取得
③BeautifulSoupメソッドで引数に指定したhtmlタグを解析し、変数に代入
④解析したhtmlタグの内、aタグをfind_allメソッドで全て抽出し、変数にリストとして代入
"""
url = 'https://kino-code.work/python-scraping/'
response = req.urlopen(url)
parse_html = BeautifulSoup(response, 'html.parser')
title_lists = parse_html.find_all('a')


"""
①抽出したaタグのタイトル（テキスト）と、urlをそれぞれ抽出したいので、空の配列を定義
②for文でリスト内の各aタグに対してタイトルとurlをappendメソッドで各配列に追加
"""
title_list = []
url_list  = []

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs['href'])


"""
①pandasでデータフレーム(TitleとURLというフレーム)を作成
②dropnaメソッドで欠損値を除外（anyの部分をallにすると、全ての値が欠損（null)の場合に除外される
③str.containsメソッドで特定の文字列が含まれているかどうか判定し、含まれる（true)値のみの新たなフレームを作成、変数に代入
④to_csvメソッドで、書き出したいデータフレームを、指定したcsvファイルに書き出す
"""
df_title_url = pd.DataFrame({'Title': title_list, 'URL': url_list})
df_notnull = df_title_url.dropna(how='any')
df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]
df_contain_python.to_csv('/Users/kotakisouichirou/Desktop/output.csv')
