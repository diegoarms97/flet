from flask import Flask, request, jsonify
import json
import logging
from werkzeug.serving import make_server
from database.session import db
from database.models.usuario import Usuario


def levantar_listening():
    print("Servidor escuchando en el puerto 8080...")
    app = Flask(__name__)
    
    # Desactiva logs HTTP por consola
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    session = db.get_session()
    
    @app.route('/hikvision/event', methods=['POST'])
    def recibir_evento():
        if 'event_log' not in request.form:
            print("⚠️ No se recibió el evento esperado.")
    
        try:
            raw_json = request.form['event_log']
            evento = json.loads(raw_json)
            evento_data = evento.get('AccessControllerEvent', {})
    
            # Verificamos si hay nombre de usuario (acceso exitoso)
            
            sub_event_type = evento_data.get("subEventType")
    
            if sub_event_type == 38:
                
                usuario=[{'tipo':'acceso con huella','name': evento_data.get('name'), 'id': evento_data.get('employeeNoString'), 
                             'fecha': evento.get('dateTime'), 'verificacion': evento_data.get('currentVerifyMode'),'resultado':'acceso exitoso',
                             }]
                session.bulk_insert_mappings(Usuario, usuario)
                session.commit()
            elif sub_event_type == 39:
                print("\n❌ Acceso denegado detectado:")
                print(evento.get('dateTime'))
            elif sub_event_type == 76:
                print("\n❌ Acceso denegado por deteccion de rostro:")
                print(evento.get('dateTime'))
            elif sub_event_type == 1024:
                print("Puerta abierta remotamente")
        except Exception as e:
            print(f"⚠️ Error procesando evento: {e}")
    
        return '', 200
        
    
    make_server("192.168.1.4", 8080, app).serve_forever()
    