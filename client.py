import requests

endpoint = 'http://localhost:8000/home'

response = requests.get(endpoint)
print(response.json())

