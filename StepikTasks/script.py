from selenium import webdriver
import time
import math

def calc(asd):
    return str(math.log(abs(12*math.sin(int(asd)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element_by_id("input_value").text
    x = calc(value)

    field = browser.find_element_by_id("answer")
    field.send_keys(x)

    
    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    time.sleep(10)
    browser.quit()