import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

class test1_unittest(unittest.TestCase):
    
    user = ''.join(random.choices(string.ascii_letters, k=6))

    def setUp(self):
        #Especificar la ruta de los controladores de chrome instalados
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_new_user(self):
        driver = self.driver
        driver.get("https://vitawines.cl/")
        driver.maximize_window()
        self.assertIn("Home | Vita Wines", driver.title)
        assert "No se encontro el elemento:" not in driver.page_source
        try:           
            login_menu = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="top_menu"]/li[6]/a'))
            )
        finally:
            login_menu.click()

        expected_page_title = "Login | Vita Wines"
        self.assertEqual(driver.title, expected_page_title, f"Se esperaba {expected_page_title}, pero se encontró {driver.title}")

        try:
            register_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[3]/div[1]/a[1]')
                )
            )
        finally:
            register_button.click()

        expected_page_title = "Sign up login | Vita Wines"
        self.assertEqual(driver.title, expected_page_title, f"Se esperaba {expected_page_title}, pero se encontró {driver.title}")

        try:
            vw_mail = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'login')))
            vw_username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'name')))
            vw_password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'password')))
            vw_confirm_password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'confirm_password')))
        finally:
            vw_mail.send_keys(self.user+"@gmail.com")
            vw_username.send_keys(self.user)
            vw_password.send_keys("Test1234")
            vw_confirm_password.send_keys("Test1234")

        try:
            sumbit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[5]/button')
                )
            )
        finally:
            sumbit_button.click()
        time.sleep(2)
        #LOGOUT TEST
        try:
            account_menu = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="top_menu"]/li[6]/a')
                )
            )
        finally:
            account_menu.click()
        try:
            logout_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="o_logout"]')
                )
            )
        finally:
            logout_button.click()
        #LOGIN TEST
        try:
            login_menu = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@href="/web/login"]')
                )
            )
        finally:
            login_menu.click()

        try:
            log_mail = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'login')))
            log_pass = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'password')))
        finally:
            log_mail.send_keys(self.user+"@gmail.com")
            log_pass.send_keys("Test1234")
        
        try:
            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[3]/button')
                )
            )
        finally:
            submit_button.click()
        time.sleep(3)
        
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
