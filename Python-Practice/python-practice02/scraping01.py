from selenium import webdriver
import time


USER = 'test_user'
PASS = 'test_pw'


#  Google Chromeを起動
browser = webdriver.Chrome() # Macの場合
browser.implicitly_wait(3)


# ログインするサイトへアクセスする
url_login = 'https://kino-code.work/membership-login'
browser.get(url_login)  # urlへ移動
time.sleep(3)  # .pyファイルにした時に処理が先に行かないようにする
print('ログインページへアクセスしました')


#  テキストボックスへ入力する
element = browser.find_element_by_id('swpm_user_name')
element.clear()
element.send_keys(USER)
element = browser.find_element_by_id('swpm_password')
element.clear()
element.send_keys(PASS)
print('フォームを送信')


#  入力したデータをクリック
browser_form = browser.find_element_by_name('swpm-login')
time.sleep(3)
browser_form.click()
print('ログインボタンを押しました')


#  ウェブサイトへアクセス
url = 'https://kino-code.work/member-only'
time.sleep(3)
browser.get(url)
print(url, ':アクセス完了')


#  ダウンロードボタンをクリック
frm = browser.find_element_by_xpath('/html/body/div/div[3]/div/main/article/div/p[2]/button')
time.sleep(1)
frm.click()
print('ダウンロードボタンをクリック')

