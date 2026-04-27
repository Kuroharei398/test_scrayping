from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome() #Chrome表示
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

table_left = driver.find_element(By.CLASS_NAME , "grid-canvas-left")
table_right = driver.find_element(By.CLASS_NAME , "grid-canvas-right")

dates = table_left.find_elements(By.CLASS_NAME , "slick-cell")
temps = table_right.find_elements(By.CLASS_NAME , "slick-cell")

for d , t in zip(dates , temps):
    print(f"{d.text} : {t.text}度")

#2秒停止
time.sleep(2)

driver.quit()