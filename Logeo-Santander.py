import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_login(self):
        driver = self.driver
        driver.get("https://www.santander.com.ar/banco/online/personas")
        time.sleep(2)

        online_banking = driver.find_element_by_xpath("//*[@id='content']/div[1]/nav[1]/div/div[3]/a[3]")
        online_banking.click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])

        dni = driver.find_element_by_name ("dni")
        dni.send_keys("*dni*")
        time.sleep(2)

        clave = driver.find_element_by_name ("clave")
        clave.send_keys ("*clave*")
        time.sleep(2)
      
        usuario = driver.find_element_by_name("usuario")
        usuario.send_keys ("*user*")
        usuario.send_keys (Keys.ENTER)
        time.sleep(4)

if __name__ == '__main__':
    unittest.main()