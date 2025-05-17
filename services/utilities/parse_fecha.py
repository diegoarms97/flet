from datetime import datetime

def parsear_fecha_biometrico(fecha_str):
    
    try:
        return datetime.fromisoformat(fecha_str)
    except Exception as e:
        print(f"[Utils] Error al parsear fecha del biométrico: {fecha_str} - {e}")
        return None
def parsear_fecha(fecha_str):
    try:
        dt = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%d/%m/%Y %H:%M")
    except Exception:
        return fecha_str  # Si falla, devuelve el original