import requests
from bs4 import BeautifulSoup
import smtplib
import os

AMAZON_LINK = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
PRICE_ALERT = 120

MY_EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')
SMTP_SERVER = os.getenv('SMTP_SERVER')

amazon_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

amazon_response = requests.get(AMAZON_LINK, headers=amazon_header)
amazon_response.raise_for_status()

soup = BeautifulSoup(amazon_response.text, 'html.parser')

price_html = soup.find('span', id='priceblock_ourprice')
price = float(price_html.string[1:])

if price <= PRICE_ALERT:
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Promotional for Amazon Item!\n\n"
                f"The Item reach below the target price of ${PRICE_ALERT}\n"
                f"Please reach the URL to access the item:\n"
                f"{AMAZON_LINK}"
        )
