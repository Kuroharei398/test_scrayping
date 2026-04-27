from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options) #Chrome表示
driver.get("https://www.data.jma.go.jp/risk/obsdl/index.php")   #該当webサイト表示
driver.implicitly_wait(3)  #全てのfind_elementで要素が見つかるまで最大3秒待機

#1秒停止
time.sleep(1)

history= driver.find_element(By.ID , "oshirase")
HTML = history.get_attribute("innerHTML")
print(f"HTML : {HTML}")

#2秒停止
time.sleep(2)

driver.quit()