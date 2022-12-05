from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search-form__input]")
search_string.send_keys("IPhone")
cnopka = browser.find_element(By.CSS_SELECTOR, "button[class*=button_color_green").click()

proverka = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*=catalog-heading]"))).text
proverka1 = "Мобильные телефоны Apple"
assert proverka == proverka1, f"Testul nu a trecut, iata ce s-a primit - {proverka}"
browser.quit()