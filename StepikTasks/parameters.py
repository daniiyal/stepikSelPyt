import pytest
from selenium import webdriver
import pytest
import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('param_link', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])

def test_answer(browser, param_link):
    link = param_link
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.implicitly_wait(10)
    area = browser.find_element_by_tag_name("textarea")
    area.send_keys(str(answer))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    feedback =  browser.find_element_by_tag_name("pre").text
    time.sleep(5)
    assert feedback == "Correct!", feedback
    