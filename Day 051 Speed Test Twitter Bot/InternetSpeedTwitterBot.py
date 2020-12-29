from selenium import webdriver
import os
import time

PROMISED_UP = 100
PROMISED_DOWN = 40
CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = None
        self.down = None
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(15)
        start_button = self.driver.find_element_by_class_name('js-start-test')
        start_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name('download-speed').text)
        self.up = float(self.driver.find_element_by_class_name('upload-speed').text)
        # self.driver.close()

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(15)

        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
        login_button.click()
        time.sleep(20)

        email_field = self.driver.find_element_by_name('session[username_or_email]')
        email_field.send_keys(EMAIL)
        pass_field = self.driver.find_element_by_name('session[password]')
        pass_field.send_keys(PASSWORD)
        enter_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
        enter_button.click()
        time.sleep(30)

        text_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span')
        text_field.send_keys(f'Download: {self.down}\nUpload: {self.up}')
        post_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        post_button.click()
