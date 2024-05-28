import os
import socket
import datetime

def servidor(socket_path):
    # Eliminar el socket si ya existe
    try:
        os.unlink(socket_path)
    except OSError:
        if os.path.exists(socket_path):
            raise

    # Crear el socket UDS
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as servidor_socket:
        # Vincular el socket a la dirección especificada
        servidor_socket.bind(socket_path)
        # Escuchar conexiones entrantes
        servidor_socket.listen()

        print("Servidor: Esperando conexiones...")

        while True:
            # Aceptar la conexión del cliente
            conexion_cliente, _ = servidor_socket.accept()
            print("Servidor: Conexión establecida.")

            # Obtener la fecha y hora actual
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Enviar la fecha y hora al cliente
            conexion_cliente.sendall(fecha_hora_actual.encode())
            print("Servidor: Fecha y hora enviadas al cliente.")

if __name__ == "__main__":
    # Especifica la ruta del socket UDS
    socket_path = "/tmp/serv4_socket"

    # Inicia el servidor
    servidor(socket_path)
