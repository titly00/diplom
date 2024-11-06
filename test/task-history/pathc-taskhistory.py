import requests

data ={
        "id": 4,
        "status_change_date": "2024-10-26T23:35:00Z",
        "old_status": "думаем",
        "new_status": "ушел из работы",
        "change_by": "выполнил",
        "task": 16
    }


response = requests.put("http://127.0.0.1:8000/taskhistorys/4/", json=data)
print(response.status_code, response.text)