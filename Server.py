import socket

class Servidor:

    print("SESIÓN SERVIDOR")

    host = "localhost"
    puerto = 65432

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.bind((host, puerto))

    serversocket.listen()
    print("Escuchando...")

    conexion, direcion_cliente = serversocket.accept()
    print('Conexión Existosa con: ', direcion_cliente)

    conexion.send(b'Hola desde el Servidor!!')
        
    print("Conexión cerrada en el servidor.")
    conexion.close()
    serversocket.close()
        
