import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjU4MzQyLCJpYXQiOjE3MjkyNTgwNDIsImp0aSI6IjIyYzkyNTBjZTViZTQzNjViODExOWNiNDhlYmE1MWQ5IiwidXNlcl9pZCI6M30.EAtmRvBtZmaqyv3f_7DwujAqu8nBoxpeFVaNIyx5DNs"
data = {
    "status_change_date": '2024-12-31-00:00',
    "old_status": "думаем",
    "new_status": "просить помощи",
    "change_by": "выполнил",
    "task": 24
}

response = requests.post("http://127.0.0.1:8000/taskhistorys/", json=data)
print(response.status_code, response.text)