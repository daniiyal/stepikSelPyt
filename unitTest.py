import unittest
from selenium import webdriver
import time






class Tests(unittest.TestCase):
    def test_1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("Name")

        last_name = browser.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("Last Name")

        email = browser.find_element_by_css_selector(".first_block .third")
        email.send_keys("E-mail")
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration Error")
        browser.quit()

    def test_2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("Name")

        last_name = browser.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("Last Name")

        email = browser.find_element_by_css_selector(".first_block .third")
        email.send_keys("E-mail")

        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration Error")

        browser.quit()

if __name__ == "__main__":
    unittest.main()