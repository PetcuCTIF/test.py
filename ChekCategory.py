# -*- coding: utf8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

name_rosetka_16_el = ['Компьютеры и ноутбуки', 'Смартфоны, ТВ и Электроника', 'Товары для геймеров', 'Бытовая техника', 'Товары для дома', 'Инструменты и автотовары', 'Сантехника и ремонт', 'Дача, сад, огород', 'Спорт и увлечения', 'Fashion', 'Красота и здоровье', 'Товары для детей', 'Зоотовары', 'Офис, школа, книги', 'Алкогольные напитки и продукты', 'Товары для бизнеса']

proverka_name = []
for index in range (0, 16):
    elements_by_rosetka = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[class*=menu-categories_type_main]>li")))
    elements_by_rosetka[index].click()

    elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.ng-star-inserted"))).text
    proverka_name.append(elements)
    time.sleep(1)
    browser.back()
assert name_rosetka_16_el == proverka_name, f"denumirile nu coincid, iata ce iese {proverka_name}"
browser.quit()


