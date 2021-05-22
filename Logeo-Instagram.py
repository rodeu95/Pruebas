import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagram(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_login(self):
        driver = self.driver
        driver.get("http://instagram.com")
        self.assertIn("Instagram", driver.title)
        time.sleep(3)

        user = driver.find_element_by_name("username")
        user.send_keys("tota.301")

        contra = driver.find_element_by_name("password")
        contra.send_keys("12281464toti")
        contra.send_keys (Keys.ENTER)
        time.sleep(3)

        info = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        info.click()

        notif = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notif.click()
        time.sleep(3)

        resultado = 'instagram' in driver.current_url
        self.assertTrue(resultado)
        assert "No se encontró el elemento: " not in driver.page_source

if __name__ == '__main__':
    unittest.main()