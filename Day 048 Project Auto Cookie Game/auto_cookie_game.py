from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

big_cookie = driver.find_element_by_id('cookie')

timeout = time.time() + 5

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:

    big_cookie.click()

    if time.time() > timeout:
        try:
            current_cookies = float(driver.find_element_by_id('money').text)
        except NoSuchElementException:
            current_cookies = 0

        products_price = driver.find_elements_by_css_selector('#store b')
        item_prices = []
        for price in products_price:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if current_cookies > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5
