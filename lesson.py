from selenium import webdriver
import math
import time

def calc(asd):
    return str(math.log(abs(12*math.sin(int(asd)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("treasure")
    value = x.get_attribute("valuex")

    
    x = calc(value)

    sdf = browser.find_element_by_id("answer")
    sdf.send_keys(x)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
