import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_find_card_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element_by_css_selector("button.btn-add-to-basket1")
        present_elem = True
    except:
        present_elem = False
    assert present_elem, "No add_card button on page"
