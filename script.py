from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.data.jma.go.jp/risk/obsdl/index.php")

driver.find_element(By.ID)