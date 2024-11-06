import requests



data = {
    "username": "Ariet",
    "password":"parol09"

}

response = requests.post("http://127.0.0.1:8000/api/token/", json=data)
print(response.status_code, response.text)


