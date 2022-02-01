import socket

class Cliente:

    print("SESIÓN CLIENTE")
    
    host = "localhost"
    puerto = 65432

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.connect((host, puerto))
    print("Conectando al servidor...")

    respuesta = socket.recv(1024)
    print(respuesta)

    print("Conexión cerrada en el cliente.")
    socket.close()
