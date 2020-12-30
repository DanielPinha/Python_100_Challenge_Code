from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get('https://www.tinder.com/')

time.sleep(15)

login_button = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

time.sleep(15)

google_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google_button.click()

time.sleep(5)

base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)

email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_input.send_keys(EMAIL)

email_next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
email_next_button.click()

time.sleep(5)

password_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(PASSWORD)

password_next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
password_next_button.click()

time.sleep(20)

driver.switch_to.window(base_window)
location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_button.click()

time.sleep(2)

notification_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
notification_button.click()

time.sleep(2)

cookies_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies_button.click()
time.sleep(1)
while True:
    like_button = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    like_button.click()
    time.sleep(1)
    try:
        super_like_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
        super_like_button.click()
    except NoSuchElementException:
        pass
    else:
        time.sleep(1)

    try:
        home_screen_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        home_screen_button.click()
    except NoSuchElementException:
        pass
    else:
        time.sleep(1)
        
    try:
        match_button = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
    except NoSuchElementException:
        pass
    else:
        time.sleep(1)
