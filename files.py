from selenium import webdriver
import time
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("input[name='firstname']")
    name.send_keys("sdfds")

    name = browser.find_element_by_css_selector("input[name='lastname']")
    name.send_keys("sdfds")

    name = browser.find_element_by_css_selector("input[name='email']")
    name.send_keys("sdfds")

    curdir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curdir)

    load = browser.find_element_by_id("file")
    load.send_keys(file_path)

    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()    