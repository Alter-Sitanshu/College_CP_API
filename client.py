import requests, getpass

# endpoint = 'http://localhost:8000/home/auth/'
# password = getpass.getpass()


# auth_response = requests.post(endpoint, json={'username':'sitanshu', 'password': password})
#token = auth_response.get('token')

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
