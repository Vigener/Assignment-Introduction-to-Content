import csv
from selenium import webdriver
import os
import time

# ChromeのWebDriverを起動
driver = webdriver.Chrome()

# スクリプトのディレクトリを取得
current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'links.csv')


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        number, link = row
        driver.get(link)

        time.sleep(5) # ページが読み込まれるのを待つ

        # 指定された番号をウィンドウで1秒間表示するアラート
        alert_text = f"{number}番目のツイートです。"
        driver.execute_script(f"alert('{alert_text}')")
        time.sleep(1)  # アラートが表示されるのを1秒待つ
        driver.switch_to.alert.accept()  # アラートを閉じる


driver.quit()  # ブラウザを閉じる
