import json

# storing BPIQ API key in credentials.py file
import credentials

import requests

url = 'https://api.bpiq.com/api/v1/drugs/'
headers = {
    'Authorization': f'Token {credentials.API_TOKEN}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
    with open("bpiq_response.json", "w+") as f:
        json.dump(data, f, indent=2)
else:
    print(f"Request failed with status code {response.status_code}")