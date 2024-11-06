

import requests

data = {

    "id": 3,
    "title": "jnih",
    "description": "выполнит",
    "start_date": "2024-05-02",
    "end_date": "2025-05-09",
    "status": "переносим задачу"

}

response = requests.put("http://127.0.0.1:8000/projects/10/", json=data)
print(response.status_code, response.text)
