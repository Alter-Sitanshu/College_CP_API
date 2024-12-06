import requests, getpass

# endpoint = 'http://localhost:8000/home/auth/'
# password = getpass.getpass()


# auth_response = requests.post(endpoint, json={'username':'sitanshu', 'password': password})
token = 'd6f59d9de9aa2a5aa52983c401aa0453c9f6e813'

headers = {
    "Authorization":f"Token {token}"
}
response = requests.post(url="http://localhost:8000/home/",
                        headers=headers,
                        json={
                            "author":'sitanshu',
                            "CF_username":'noob_croc',
                            "CF_rating":532
                        })
print(response.json())
