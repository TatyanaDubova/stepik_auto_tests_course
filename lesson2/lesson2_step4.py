from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Найдём этот элемент с помощью WebDriver:
    x_element = browser.find_element_by_id("treasure")
    # Найдём атрибут "valuex" с помощью встроенного метода get_attribute:
    x_valuex = x_element.get_attribute("valuex")
    # значение атрибута "valuex" помещаем в переменную "x"
    x = x_valuex
    print(x)
    y = calc(x)
    print(y)
    # Поместить ответ в строку
    browser.find_element_by_id("answer").send_keys(y)
    # Поменять чекбокс и радиобатон на нужные
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
