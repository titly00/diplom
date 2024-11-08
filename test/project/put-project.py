import requests

data = {

    "title": "maksim",
    "description": "думаеm",
    "start_date": "2024-10-06",
    "end_date": "2025-04-09",
    "status": "сделал"

}

response = requests.put("http://127.0.0.1:8000/projects/5/", json=data)
print(response.status_code, response.text)
