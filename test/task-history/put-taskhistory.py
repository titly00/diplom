import requests

data ={

        "status_change_date": "2024-10-26T23:35:00Z",
        "old_status": "выполнил",
        "new_status": "дали новою задачу",
        "change_by": "переносить задачу",
        "task": 23
    }


response = requests.put("http://127.0.0.1:8000/taskhistorys/7/", json=data)
print(response.status_code, response.text)