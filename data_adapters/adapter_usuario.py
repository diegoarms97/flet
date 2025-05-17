import requests
from requests.auth import HTTPDigestAuth
from services.utilities.parse_fecha import parsear_fecha_biometrico
from datetime import datetime
def obtener_datos_usuario_desde_biometrico(usuario_id):
    url = "http://192.168.1.2/ISAPI/AccessControl/UserInfo/Search?format=json"
    headers = {"Content-Type": "application/json"}
    payload = {
        "UserInfoSearchCond": {
            "searchID": "1",
            "searchResultPosition": 0,
            "maxResults": 1,
            "EmployeeNo": {
                "value": str(usuario_id)  
        }
    }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5, auth=HTTPDigestAuth("admin", "Acceso2025"))
        response.raise_for_status()
        data = response.json()

        user_list = data.get("UserInfoSearch", {}).get("UserInfo", [])
        if not user_list:
            return None

        usuario = user_list[0]
        
        return {
            "usuario_id": usuario.get("employeeNo"),
            "nombre": usuario.get("name"),
            "correo": "email",  # Si el biométrico no lo tiene, regresa None
            "fecha_registro": datetime.now()  
        }

    except requests.RequestException as e:
        print(f"[usuario_adapter] Error al consultar biométrico: {e}")
        return None
