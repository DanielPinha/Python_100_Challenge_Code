import requests
import os
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = os.getenv('TEQUILA_ENDPOINT')
TEQUILA_AUTH = os.getenv('TEQUILA_AUTH')

tequila_header = {
    'apikey': TEQUILA_AUTH,
    'Content-Type': 'application/json',
}


class FlightSearch:
    def __init__(self):
        self.fly_from = 'LCY'
        self.fly_to = ''
        # (dd/mm/yyyy)
        self.date_from = datetime.now().date().strftime('%d/%m/%Y')
        self.date_to = (datetime.now().date() + timedelta(weeks=26)).strftime('%d/%m/%Y')
        self.max_price = None
        self.tequila_params = {
            'fly_from': self.fly_from,
            'fly_to': self.fly_to,
            'price_to': self.max_price,
            'date_from': self.date_from,
            'date_to': self.date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
        }
        self.search_result = None

    def update_api_params(self):
        """Update Params to be sent to API GET request"""
        self.tequila_params = {
            'fly_from': self.fly_from,
            'fly_to': self.fly_to,
            'price_to': self.max_price,
            'date_from': self.date_from,
            'date_to': self.date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
        }

    def search_flight(self):
        """Get Request for flights"""
        self.update_api_params()
        response = requests.get(url=TEQUILA_ENDPOINT, headers=tequila_header, params=self.tequila_params)
        response.raise_for_status()
        self.search_result = response.json()
        # In case empty data is returned
        if not self.search_result['data']:
            self.search_result = None
