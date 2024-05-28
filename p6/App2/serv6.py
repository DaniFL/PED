import socket
from datetime import datetime

def start_server(host='localhost', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor escuchando en {host}:{port}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Conexión recibida de {addr}")
            message = client_socket.recv(1024).decode()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Mensaje recibido: {message} a las {current_time}")
            response = f"Mensaje recibido a las {current_time}: {message}"
            client_socket.send(response.encode())
            client_socket.close()
    except KeyboardInterrupt:
        print("Servidor terminando...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()
