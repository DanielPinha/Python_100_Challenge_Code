from selenium import webdriver
from bs4 import BeautifulSoup
import time

FORMS_LINK = 'https://forms.gle/efLp38DRWCNNZUxD8'
NETIMOVEIS_LINK = 'https://www.netimoveis.com/locacao/bahia/salvador/apartamento?cmp=715&3Ftipo%3Dapartamento=&transacao=locacao&localizacao=BR-BA-salvador---&tipo=apartamento&utm_source=Google&utm_medium=cpc&utm_campaign=mol&gclid=CjwKCAiAirb_BRBNEiwALHlnDwUMkChpkln3G9RWQn0tzYkpXDs2G2uNQoeWA1AjDn1-EfaNZ2pr9BoC8gAQAvD_BwE&valorMax=3000&pagina=1'

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(NETIMOVEIS_LINK)
imoveis_response = driver.page_source

soup = BeautifulSoup(imoveis_response, 'html.parser')

address_list = [address.getText() for address in soup.find_all('div', class_='endereco')]
price_list = [value.getText().split(' ')[-1].replace(u'\xa0', u' ') for value in soup.find_all('div', class_='valor')]
link_list = [url['href'] for url in soup.find_all('a', class_='link-imovel')]


for index in range(0, len(price_list)-1):
    driver.get(FORMS_LINK)
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

    time.sleep(5)
    address_input.send_keys(address_list[index])
    price_input.send_keys(price_list[index])
    link_input.send_keys(link_list[index])
    submit_button.click()

driver.quit()
