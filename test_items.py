from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Basket button does not exist"