from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'


class InstaFollower:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.email = email
        self.password = password

    def login_insta(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(10)
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys(self.email)
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(self.password)
        enter_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        enter_button.click()

        time.sleep(10)
        login_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        login_info.click()

        time.sleep(10)
        notification_warning = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_warning.click()

    def find_followers(self, search):
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(search)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(10)

    def follow(self):
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
        follows = self.driver.find_elements_by_class_name('sqdOP')
        for follow in follows:
            if follow.text == 'Seguir':
                time.sleep(2)
                follow.click()
