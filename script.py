from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from openpyxl import Workbook
from openpyxl.chart import LineChart , Reference
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options) #Chrome表示
driver.get("https://www.data.jma.go.jp/risk/obsdl/index.php")   #該当webサイト表示
driver.implicitly_wait(3)  #全てのfind_elementで要素が見つかるまで最大3秒待機

#1秒停止
time.sleep(1)

#東京の「東京」をクリック
btn_tokyo_1 = driver.find_element(By.ID , "pr44")
btn_tokyo_1.click()
btn_tokyo_2 = driver.find_element(By.CSS_SELECTOR , "#stationMap > div:nth-child(10) > div")
btn_tokyo_2.click()

#ID属性の要素を取得(項目を選ぶをクリック)
btn_element = driver.find_element(By.ID , "elementButton")
btn_element.click()

#日別値→日平均気温をクリック
radio_by_day = driver.find_element(By.CSS_SELECTOR , "#aggrgPeriod > div > ul > li:nth-child(2) > label > span")
radio_by_day.click()
radio_avgtemp = driver.find_element(By.ID , "平均気温")
radio_avgtemp.click()

#「期間を選ぶ」をクリック
btn_period = driver.find_element(By.ID , "periodButton")
btn_period.click()

#開始年月日のプルダウン取得
pulldown_ini_y = driver.find_element(By.NAME , "iniy")
Select(pulldown_ini_y).select_by_visible_text("2026")

pulldown_ini_m = driver.find_element(By.NAME , "inim")
Select(pulldown_ini_m).select_by_visible_text("1")

pulldown_ini_d = driver.find_element(By.NAME , "inid")
Select(pulldown_ini_d).select_by_visible_text("1")

#終了年月日のプルダウン取得
pulldown_end_y = driver.find_element(By.NAME , "endy")
Select(pulldown_end_y).select_by_visible_text("2026")

pulldown_end_m = driver.find_element(By.NAME , "endm")
Select(pulldown_end_m).select_by_visible_text("1")

pulldown_end_d = driver.find_element(By.NAME , "endd")
Select(pulldown_end_d).select_by_visible_text("31")

#「画面に表示」をクリック
btn_display = driver.find_element(By.CSS_SELECTOR , "#loadTable > img")
btn_display.click()

#日付・温度を取得
table_left = driver.find_element(By.CLASS_NAME , "grid-canvas-left")
table_right = driver.find_element(By.CLASS_NAME , "grid-canvas-right")

dates = table_left.find_elements(By.CLASS_NAME , "slick-cell")
temps = table_right.find_elements(By.CLASS_NAME , "slick-cell")

#データ整形
#seleniumで取得したデータを、リスト内方表記を使用して表示されている文字のみを抜き出す
date_list = [d.text[5:] for d in dates]
#空文字の場合はNoneを、それ以外の場合はtempsのデータを数値型に変換(excelで使えるデータへ)
temp_list = [float(t.text) if t.text != "" else None for t in temps]

#Excel作成
wb = Workbook() #シート1枚のExcelファイル作成
ws = wb.active  #現在表示しているシートを取得
ws.title = "2026_01_気温データ"  #シートタイトル

#ヘッダー
ws.append(["日付", "平均気温"])

# データ書き込み
for d, t in zip(date_list, temp_list):
    ws.append([d, t])

# --- グラフ作成 ---
chart = LineChart() #空の折れ線グラフ作成
chart.title = "2026年1月 東京 平均気温（℃）" #グラフタイトル
chart.y_axis.title = None #縦軸のラベル(表示しない)
chart.x_axis.title = "日付" #横軸のラベル

# データ範囲（2列目が気温）
data = Reference(ws, min_col=2, min_row=1, max_row=len(temp_list)+1)    #ヘッダー含むB列1行目以降の平均気温を指定
# 日付（1列目）
cats = Reference(ws, min_col=1, min_row=2, max_row=len(date_list)+1)    #A列2行目以降の日付を指定

#グラフに平均気温を挿入
chart.add_data(data, titles_from_data=True)

chart.y_axis.number_format = '0.0"℃"'   #度数表示
chart.y_axis.majorUnit = 1  #1度間隔
chart.y_axis.crosses = "min"    #軸を左端固定
chart.y_axis.delete = False     #数値強制表示
#横軸へ日付を挿入
chart.set_categories(cats)

# シートにグラフ追加
chart.width = 30    #横幅
chart.height = 23   #高さ
chart.x_axis.tickLblSkip = 1    #横軸ラベル全表示
ws.add_chart(chart, "E3")

# 保存
wb.save("tokyo_temp_202601.xlsx")

#2秒停止
time.sleep(2)

driver.quit()