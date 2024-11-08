import requests

data = {
    "title": "Тариэл",
    "description": "красава учиться",
    "start_date": "2024-09-11",
    "end_date": "2024-11-11",
    "status": "Новичок"
}
for i in range(3):
    print(i)
    response = requests.post('http://127.0.0.1:8000/projects/', json=data)
    print(response.status_code, response.text)
