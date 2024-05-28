import socket

def cliente(socket_path):
    # Conectar al socket UDS del servidor
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect(socket_path)
        print("Cliente: Conexión establecida con el servidor.")

        # Recibir la fecha y hora del servidor
        fecha_hora_servidor = cliente_socket.recv(1024).decode()
        print("Cliente: Fecha y hora recibidas del servidor:", fecha_hora_servidor)

if __name__ == "__main__":
    # Especifica la ruta del socket UDS
    socket_path = "/tmp/serv4_socket"

    # Inicia el cliente
    cliente(socket_path)

