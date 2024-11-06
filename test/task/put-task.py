import requests

url = 'http://127.0.0.1:8000/tasks/'



file_path = 'maxresdefault.jpg'

data = {
    "title": "ari",
    "description": "pap",
    "start_date": "2024-10-31",
    "end_date": "2024-12-27",
    "project": 1,
    "assigned_users": [
            4
      ]
}


response = requests.post("http://127.0.0.1:8000/tasks/", json=data)
print(response.status_code, response.text)

with open(file_path, "rb") as f:
    files = {"files": f}
    response = requests.post(url, data=data, files=files)

# Обрабатываем ответ
if response.status_code == 201:
    print("Resume uploaded successfully.")
    print("Response data:", response.json())
else:
    print(f"Failed to upload resume. Status code: {response.status_code}")
    print("Error response:", response.text)

