import socket
from datetime import datetime

def start_client(server_host='localhost', server_port=8080, message="Hola servidor!"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_host, server_port))
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"{message} (enviado a las {current_time})"
        client_socket.send(full_message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    start_client()
