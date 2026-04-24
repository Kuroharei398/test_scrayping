from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome() #Chrome表示
driver.get("https://www.data.jma.go.jp/risk/obsdl/index.php")   #該当webサイト表示
#wait = WebDriverWait(driver , 10)   #タイムアウト10秒
driver.implicitly_wait(3)  #全てのfind_elementで要素が見つかるまで最大3秒待機

#1秒停止
time.sleep(1)

#要素が表示されるまで待機(今回は最大10秒)
#wait.until(EC.visibility_of_element_located((By.ID , "elementButton")))
#ID属性の要素を取得(項目を選ぶをクリック)
btn_element = driver.find_element(By.ID , "elementButton")
btn_element.click()

tab_temp = driver.find_element(By.ID , "temptab")   #気温タブ取得
temp_eles = tab_temp.find_elements(By.TAG_NAME , "label")   #ラベル全取得
for t in temp_eles:
    t.click()   #全てのラベルに対してクリック処理

#「期間を選ぶ」をクリック
btn_period = driver.find_element(By.ID , "periodButton")
btn_period.click()

#開始年のプルダウン取得
pulldown_iniy = driver.find_element(By.NAME , "iniy")
pulldown_iniy.click()

#「画面に表示」をクリック
#btn_display = driver.find_element(By.CSS_SELECTOR , "#loadTable > img")
#btn_display.click()

#2秒停止
time.sleep(2)

driver.quit()