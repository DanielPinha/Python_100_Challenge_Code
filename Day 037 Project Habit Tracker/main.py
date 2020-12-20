import requests
import os
from datetime import datetime

PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
PIXELA_USERNAME = os.getenv('PIXELA_USER')

pixela_endpoint = 'https://pixe.la/v1/users'
pixela_params = {
    "token": PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=pixela_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Code Graph",
    "unit": "Code",
    "type": "int",
    "color": "ajisai",
}

headers = {
    'X-USER-TOKEN': PIXELA_TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

graph1_endpoint = f"{graph_endpoint}/graph1"

graph1_config = {
    # 'date': ''.join(str(datetime.now().date()).split('-')),
    'date': datetime.now().strftime('%Y%m%d'),
    'quantity': input("How much have you coded? "),
}

response = requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)
print(response.text)

# put_pixel_endpoint = f"{graph1_endpoint}/{graph1_config['date']}"
#
# put_pixel_params = {
#     'quantity': '5'
# }
#
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
# print(response.text)
#
# delete_endpoint = put_pixel_endpoint
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)