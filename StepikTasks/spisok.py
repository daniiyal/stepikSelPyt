from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_id("num1").text
    second = browser.find_element_by_id("num2").text

    sum = str(int(first) + int(second))

    
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_visible_text(sum)

    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()