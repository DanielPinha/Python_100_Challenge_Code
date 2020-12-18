import requests
import smtplib

# ---------- CREATE CONSTANT ---------- #
MY_EMAIL = 'YOUR_EMAIL@gmail.com'
PASSWORD = 'EMAIL_PASSWORD'
SMTP_SERVE = 'smtp.gmail.com'
WEATHER_API_KEY = 'API kEY'
LATITUDE = -12.974722
LONGITUDE = -38.476665

# ---------- Send email for Umbrella Reminder ---------- #


def send_email():
    with smtplib.SMTP(SMTP_SERVE) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:It is raining man!\n\nAleluia! and bring an umbrella, please"
        )


# --------------- GET WEATHER INFO --------------- #


weather_param = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': WEATHER_API_KEY,
    'units': 'metric',
    'exclude': 'current,minutely,daily'
}

weather_api = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=weather_param)
weather_api.raise_for_status()
weather_data_hour = weather_api.json()['hourly']

weather_12_hours = weather_data_hour[:12]
# --------------- CHECK IF RAIN IN NEXT 12 HOURS --------------- #
for item in weather_12_hours:
    if item['weather'][0]['id'] < 700:
        send_email()
        break
