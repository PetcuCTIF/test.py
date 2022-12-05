import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://magnat.md/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

x = browser.find_element(By.XPATH, "//input[@aria-label='Search']")
x.send_keys("Батарейка")
browser.find_element(By.CSS_SELECTOR, "button[class*=searchsubmit]").click()
browser.find_element(By.XPATH, "//a[@data-product_sku='E3703']").click()
# browser.find_element(By.XPATH, "//a[@data-product_sku='66638']").click()
browser.find_element(By.XPATH, "//a[@data-product_sku='58419BW']").click()
# browser.find_element(By.XPATH, "//a[@data-product_sku='R6BER/8PR']").click()
browser.find_element(By.XPATH, "//a[@title='КОРЗИНА']").click()
time.sleep(3)
browser.find_element(By.CSS_SELECTOR, "a[class*=cookies-accept-btn]").click()
browser.find_element(By.CSS_SELECTOR, "a[class*=checkout]").click()
x = browser.find_element(By.XPATH, "//input[@name='billing_first_name']")
x.send_keys("Petcu Test")
x = browser.find_element(By.XPATH, "//input[@name='billing_address_1']")
x.send_keys("Nu va speriati, eu ma joc -))")
x = browser.find_element(By.XPATH, "//input[@name='billing_phone']")
x.send_keys("+373696")
x = browser.find_element(By.XPATH, "//input[@name='billing_email']")
x.send_keys("alex.petku@gmail.com")
x = browser.find_element(By.XPATH, "//textarea[@name='order_comments']")
x.send_keys("Buna ziua fetitzele, nu atrageti atentia, eu doar ma invat sa ma (coviresc) prin saituri fara sa le accesez. Felicitari cu prima zi de iarna ;)")
x = browser.find_element(By.XPATH, "//input[@name='terms']")
x.click()

# browser.find_element(By.CSS_SELECTOR, "button[name*=woocommerce_checkout_place_order]").click()
# browser.quit()


