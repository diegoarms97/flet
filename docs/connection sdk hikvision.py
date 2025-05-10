import ctypes

# Cargar la librería del SDK Este script es un prototipo y no se puede ejecutar, habria que revisar la documentacion especifica del biometrico
sdk_path = "C:\\Ruta\\Al\\SDK\\HikSDK.dll"
sdk = ctypes.WinDLL(sdk_path)

# Inicializar el SDK
if sdk.SDK_Init() != 0:
    print("Error al inicializar el SDK")
else:
    print("SDK inicializado correctamente")

# Conectar con el dispositivo

ip = b"192.168.1.100"
puerto = 8000
usuario = b"admin"
contraseña = b"password"
session = sdk.ConnectDevice(ip, puerto, usuario, contraseña)
if session == 0:
    print("Error al conectar con el dispositivo")
else:
    print("Conexión establecida, sesión:", session)

# Obtener registros biométricos 
# La estructura y la forma de llamada dependerán de la documentación
registro = sdk.GetBiometricRecords(session)
print("Registros biométricos:", registro)

# Cerrar sesión y limpiar recursos
sdk.DisconnectDevice(session)
sdk.SDK_Cleanup()
