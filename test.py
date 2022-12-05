from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
input_google = driver.find_element_by_xpath('//input[@name="q"]')
input_google.send_keys("Iphone")
input_google.send_keys(Keys.RETURN)
assert "Iphone - Поиск в Google" in driver.title
