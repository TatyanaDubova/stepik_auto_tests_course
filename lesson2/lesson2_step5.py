from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    num_1 = browser.find_element_by_id("num1")
    num_2 = browser.find_element_by_id("num2")
    x = int(num_1.text)
    y = int(num_2.text)
    sum = x+y
    print(sum)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    sum = str(sum)
    select.select_by_visible_text(sum)  # ищем элемент по тексту равный рассчитаной сумме в переменной sum

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
