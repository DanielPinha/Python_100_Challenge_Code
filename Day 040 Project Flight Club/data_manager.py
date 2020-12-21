import requests
import os

SHEETY_DEALS_ENDPOINT = os.getenv('SHEETY_DEALS_ENDPOINT')
SHEETY_DEALS_AUTH = os.getenv('SHEETY_DEALS_AUTH')

SHEETY_USER_ENDPOINT = os.getenv('SHEETY_USER_ENDPOINT')
SHEETY_USER_AUTH = os.getenv('SHEETY_USER_AUTH')

sheety_deals_header = {
    'Content-Type': 'application/json',
    'Authorization': SHEETY_DEALS_AUTH,
}

sheety_user_header = {
    'Content-Type': 'application/json',
    'Authorization': SHEETY_USER_AUTH,
}


class DataManager:

    def __init__(self):
        response = requests.get(url=SHEETY_DEALS_ENDPOINT, headers=sheety_deals_header)
        response.raise_for_status()
        self.deals = response.json()
        self.get_new_user_list()
        self.add_user_status = None

    def add_in_user_database(self, name, last_name, email):
        user_param = {
            'email': {
                'name': name,
                'lastName': last_name,
                'email': email,
            }
        }
        requests.post(url=SHEETY_USER_ENDPOINT, headers=sheety_user_header, json=user_param)
        self.get_new_user_list()

    def get_new_user_list(self):
        response = requests.get(url=SHEETY_USER_ENDPOINT, headers=sheety_user_header)
        response.raise_for_status()
        self.emails = response.json()
