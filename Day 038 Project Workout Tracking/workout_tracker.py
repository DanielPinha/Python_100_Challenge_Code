import requests
import os
from datetime import datetime

# ------------------------- READ NATURAL LANGUAGE INPUT ------------------------- #
NUTRI_ID = os.getenv('NUTRI_ID')
NUTRI_KEY = os.getenv('NUTRI_KEY')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

nutri_header = {
    'x-app-id': NUTRI_ID,
    'x-app-key': NUTRI_KEY,
    'Content-Type': 'application/json',
}

nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutri_json = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 175.04,
    "age": 24,
}

nutri_response = requests.post(url=nutri_endpoint, headers=nutri_header, json=nutri_json)
nutri_response.raise_for_status()

# ------------------------- READ EXERCISE DONE AND UPDATED GOOGLE SHEET ------------------------- #
sheety_header = {
    'Content-Type': 'application/json',
    'Authorization': SHEETY_AUTH,
}

for exercise in nutri_response.json()['exercises']:
    sheety_json = {
        'workout': {
            'date': str(datetime.now().date().strftime('%d/%m/%Y')),
            'time': str(datetime.now().time().strftime('%H:%M:%S')),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_header, json=sheety_json)
    sheety_response.raise_for_status()
