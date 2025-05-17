import requests
from requests.auth import HTTPDigestAuth

url = "http://192.168.1.2/ISAPI/AccessControl/UserInfo/Search?format=json"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "UserInfoSearchCond": {
        "searchID": "1",
        "searchResultPosition": 0,
        "maxResults": 1,
        "EmployeeNo": {
            "value": 1  # Cambia esto por el ID del usuario que deseas buscar
        }
    }
}

response = requests.post(url, json=payload, headers=headers, auth=HTTPDigestAuth("admin", "Acceso2025"))

print(response.status_code)
print(response.)
