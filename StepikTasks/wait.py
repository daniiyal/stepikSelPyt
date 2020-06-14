from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(asd):
    return str(math.log(abs(12*math.sin(int(asd)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button#book')
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x = browser.find_element_by_id("input_value").text
    value = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(value)

    btn = browser.find_element_by_css_selector("button#solve")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()