import requests


data = {
    "user": 4,
    "name": "Ariety",
    "robot": "read code",
    "register": "site"

}


response = requests.post('http://127.0.0.1:8000/register/', json=data)
print(response.status_code, response.text)