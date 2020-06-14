from selenium import webdriver
import time
import math

def calc(asd):
    return str(math.log(abs(12*math.sin(int(asd)))))


try:
    link =  "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_class_name("trollface")
    btn.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)

    x = browser.find_element_by_id("input_value").text
    value = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(value)

    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()