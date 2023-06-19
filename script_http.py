## Basic script to make http request with headers or params and display the response as an indented json

import requests
import json

url = 'https://cat-fact.herokuapp.com/facts/random'

headers = {
    'header1': 'value1',
    'header2': 'value2'
}

params = {
    'param1': 'value1',
    'param2': 'value2'
}

response = requests.get(url, headers=headers, params=params)

parsed_json = response.json()

print('Status code:', response.status_code)
#displays json with readable indentation
print('Response content:', json.dumps(parsed_json, indent=4))
