from selenium import webdriver
import time
import TestAbs

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
    input3.send_keys("email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text
    print(welcome_text)
    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

finally:
    time.sleep(5)
    browser.quit()
