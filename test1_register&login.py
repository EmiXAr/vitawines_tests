from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import string
import random

#Especificar la ruta de los controladores de chrome instalados
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://vitawines.cl/")
driver.maximize_window()

login_menu = driver.find_element(By.XPATH, '//a[@href="/web/login"]')
login_menu.click()

register_button = driver.find_element(By.XPATH, '//a[@href="/web/signup"]')
register_button.click()

vw_mail = driver.find_element(By.ID, 'login')
vw_username = driver.find_element(By.ID, 'name')
vw_password = driver.find_element(By.ID, 'password')
vw_confirm_password = driver.find_element(By.ID, 'confirm_password')

def generate_user():
    n = 6
    username = ''.join(random.choices(string.ascii_letters, k=n))
    return username
user = generate_user()

vw_mail.send_keys(user+"@gmail.com")
vw_username.send_keys(user)
vw_password.send_keys("Test1234")
vw_confirm_password.send_keys("Test1234")

submit_button = driver.find_element(By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[5]/button')
submit_button.click()
time.sleep(1)

account_menu = driver.find_element(By.XPATH, '//*[@id="top_menu"]/li[5]/a')
account_menu.click()

logout_button = driver.find_element(By.XPATH, '//*[@id="o_logout"]')
logout_button.click()

login_menu = driver.find_element(By.XPATH, '//a[@href="/web/login"]')
login_menu.click()

log_mail = driver.find_element(By.ID, 'login')
log_pass = driver.find_element(By.ID, 'password')
log_mail.send_keys(user+"@gmail.com")
log_pass.send_keys("Test1234")

submit_button = driver.find_element(By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[3]/button')
submit_button.click()
time.sleep(2)

driver.close()
