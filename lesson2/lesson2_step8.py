from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import os

    # Kод, который заполняет обязательные поля по атрибуту name
    browser.find_element_by_name("firstname").send_keys("First name")
    browser.find_element_by_name("lastname").send_keys("Last name")
    browser.find_element_by_name("email").send_keys("Email")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()