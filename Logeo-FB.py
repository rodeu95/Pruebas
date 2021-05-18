import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_logeoFB(self):
        driver = self.driver
        driver.get("http://facebook.com")
        time.sleep(2)

        user = driver.find_element_by_name("email")
        user.send_keys("#mail")

        contra = driver.find_element_by_name("pass")
        contra.send_keys("#contraseña")
        contra.send_keys(Keys.ENTER)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()