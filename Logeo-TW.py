import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class twitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_logeoTW(self):
        driver = self.driver
        driver.get("http://twitter.com/login")
        time.sleep(2)

        user = driver.find_element_by_name("session[username_or_email]")
        user.send_keys("#user")

        contra = driver.find_element_by_name("session[password]")
        contra.send_keys("#clave")
        contra.send_keys(Keys.ENTER)
        time.sleep(2)

        urlTwitter = 'https://twitter.com/home'
        urlActual = driver.current_url
        self.assertEqual(urlTwitter,urlActual)
    
    def test_error(self):
        driver = self.driver
        driver.get("http://twitter.com/login")
        time.sleep(2)

        user = driver.find_element_by_name("session[username_or_email]")
        user.send_keys("#user")

        contra = driver.find_element_by_name("session[password]")
        contra.send_keys("#claveErronea")
        contra.send_keys(Keys.ENTER)
        time.sleep(2)

        resultado = 'error' in driver.current_url
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
    