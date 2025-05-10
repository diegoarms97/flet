import socket
#Script para adaptar los comandos del dispositivo zkteco a un servidor http

device_ip = '192.168.1.100'
port = 4370  

try:
    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((device_ip, port))
        print("Conexión establecida con el dispositivo Skyeko F16")

        # Enviar un comando al dispositivo
        comando = "COMANDO"
        s.sendall(comando.encode('utf-8'))

        # Recibir la respuesta
        response = s.recv(1024)
        print("Respuesta del dispositivo:", response.decode('utf-8'))
except Exception as e:
    print("Error al conectar o comunicarse con el dispositivo:", e)
