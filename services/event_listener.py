# services/event_listener.py
from flask import Flask, request
import json
from werkzeug.serving import make_server
import threading


from data_adapters.adapter_log_acceso import recibir_log_desde_biometrico

app = Flask(__name__)

BIOMETRICO_IP = "192.168.1.2"  # IP del dispositivo biométrico autorizado


@app.route('/hikvision/event', methods=['POST'])
def recibir_evento():
    # Validación de IP de origen
    if request.remote_addr != BIOMETRICO_IP:
        print(f"⚠️ Conexión rechazada desde IP no autorizada: {request.remote_addr}")
        return '', 403

    if 'event_log' not in request.form:
        return '', 400

    try:
        print("🔔 Evento recibido del biométrico")
        raw_json = request.form['event_log']
        evento = json.loads(raw_json)
        evento_data = evento.get('AccessControllerEvent', {})
        sub_event_type = evento_data.get("subEventType")
        print(f"🔍 Tipo de evento: {sub_event_type}")

        if sub_event_type == 38:  # Acceso exitoso
            

            log_data = {
                "usuario_id": evento_data.get("employeeNoString"),
                "fecha_hora": evento.get("dateTime"),
                "tipo_evento": "Acceso",
                "resultado": "Permitido"
            }
            
            recibir_log_desde_biometrico(log_data)

        elif sub_event_type in [39, 76]:  # Acceso denegado
            log_data = {
                "usuario_id_externo": evento_data.get("employeeNoString", None),
                "fecha_hora": evento.get("dateTime"),
                "tipo_evento": "Acceso",
                "resultado": "Denegado"
            }
            recibir_log_desde_biometrico(log_data)

        elif sub_event_type == 1024:  # Apertura remota
            print("🔓 Puerta abierta remotamente (subEventType 1024)")
            log_data = {
                "usuario_id_externo": evento_data.get("employeeNoString", None),
                "fecha_hora": evento.get("dateTime"),
                "tipo_evento": "Apertura remota",
                "resultado": "Permitido"
            }
            recibir_log_desde_biometrico(log_data)

    except Exception as e:
        print(f"⚠️ Error procesando evento: {e}")

    return '', 200


def levantar_listening():
    def run():
        make_server("192.168.1.3", 8080, app).serve_forever()

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
