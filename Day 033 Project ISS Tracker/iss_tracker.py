import requests
from datetime import datetime
import smtplib
import time
# -------------- CREATE CONSTANT -------------- #
MY_LAT = -12.977749
MY_LONG = -38.501629
MY_EMAIL = 'danielpinhapog@gmail.com'
PASSWORD = 'pogtrial123'
SMTP_SERVE = 'smtp.gmail.com'
# -------------- SEND EMAIL -------------- #


def send_email():
    with smtplib.SMTP(SMTP_SERVE) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS Satellite!\n\nLook Up"
        )


# -------------- GET SATELLITE INFORMATION -------------- #
def is_sat_overhead():
    sat_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    sat_response.raise_for_status()
    sat_data = sat_response.json()

    sat_lat = round(float(sat_data['iss_position']['latitude']), 1)
    sat_long = round(float(sat_data['iss_position']['longitude']), 1)

    if round(MY_LAT, 1) == sat_lat and round(MY_LONG, 1) == sat_long:
        return True


# -------------- GET SUNSET and SUNRISE TIME -------------- #
def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    sun_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    sunrise_hour = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_hour = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])

    # -------------- GET CURRENT HOUR -------------- #
    current_hour = datetime.now().hour

    if sunset_hour < current_hour or current_hour < sunrise_hour:
        return True


# -------------- EVALUATE IF NIGHT TIME AND SATELLITE OVER CITY -------------- #
while True:
    time.sleep(60)
    if is_night() and is_sat_overhead():
        send_email()
