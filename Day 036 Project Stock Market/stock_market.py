import os
import requests
import smtplib

# -------------------- DEFINE CONSTANT VARIABLES  -------------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
EMAIL_USER = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
SMTP_SERVER = os.getenv('SMTP_SERVER')

# -------------------- GET COMPANY THREE LATEST ARTICLES -------------------- #


def get_news():
    news_parameters = {
        'q': COMPANY_NAME,
        'apiKey': os.getenv('NEWS_KEY'),
        'language': 'en',
    }

    news_api = requests.get(url='https://newsapi.org/v2/everything', params=news_parameters)
    news_api.raise_for_status()

    return news_api.json()['articles'][:3]


# -------------------- Send Email with stock fluctuation and News -------------------- #


def send_email(stock_diff, news):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=EMAIL_USER,
            msg=f"Subject:Big fluctuation for {COMPANY_NAME} stock!\n\n"
                f"Stock: {STOCK}\n"
                f"Last two openings fluctuation: {round(stock_diff, 2)}%\n"
                f"Latest News:\n"
                f"  {news[0]['title']}\n"
                f"  {news[0]['author']}\n"
                f"  {news[0]['publishedAt']}\n"
                f"  {news[0]['url']}\n\n"
                f"  {news[1]['title']}\n"
                f"  {news[1]['author']}\n"
                f"  {news[1]['publishedAt']}\n"
                f"  {news[1]['url']}\n\n"
                f"  {news[2]['title']}\n"
                f"  {news[2]['author']}\n"
                f"  {news[2]['publishedAt']}\n"
                f"  {news[2]['url']}\n\n"
        )


# -------------------- GET STOCK INFORMATION FROM LAST TWO DAYS -------------------- #
alpha_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': os.getenv('ALPHA_KEY')
}
alpha_api = requests.get(url='https://www.alphavantage.co/query', params=alpha_parameters)
alpha_api.raise_for_status()

stock_data = alpha_api.json()['Time Series (Daily)']
two_last_days = list(stock_data.keys())[:2]

stock_current_day_value = float(stock_data[two_last_days[0]]['1. open'])
stock_last_day_value = float(stock_data[two_last_days[1]]['1. open'])
stock_value_diff = (stock_current_day_value - stock_last_day_value) / stock_current_day_value * 100

# -------------------- EVALUATE IF STOCK FLUCTUATION REACH OVER 5% -------------------- #
if abs(stock_value_diff) >= 5.0:
    send_email(stock_value_diff, get_news())
