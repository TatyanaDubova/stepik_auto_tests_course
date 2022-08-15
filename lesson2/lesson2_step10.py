from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    # Ввести ответ в поле
    browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
