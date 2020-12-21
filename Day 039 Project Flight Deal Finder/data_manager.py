import requests
import os

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

sheety_header = {
    'Content-Type': 'application/json',
    'Authorization': SHEETY_AUTH,
}


class DataManager:

    def __init__(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
        response.raise_for_status()
        self.deals = response.json()
