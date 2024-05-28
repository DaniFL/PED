import socket
import os
import sys
import signal

def main():
    original_stdout = sys.stdout

    # Si la salida estándar no está redirigida, imprime los mensajes de solicitud de entrada
    if sys.stdout.isatty():
        host = 'localhost'
        port = int(input("Ingrese el puerto en el que el servidor deberá escuchar: "))
    else:
        # Si la salida estándar está redirigida, no solicita la entrada del usuario
        host = 'localhost'
        port = int(input())

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    # Imprime los mensajes en la consola incluso si la salida estándar está redirigida
    sys.stdout.write(f"Servidor escuchando en {host}:{port}\n")
    sys.stdout.flush()

    try:
        while True:
            conn, addr = server_socket.accept()
            # Imprime los mensajes en la consola incluso si la salida estándar está redirigida
            sys.stdout.write(f"Conectado con {addr}\n")
            sys.stdout.flush()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    filepath = data.decode()
                    if filepath.lower() == 'exit':
                        # Imprime los mensajes en la consola incluso si la salida estándar está redirigida
                        sys.stdout.write("Comando de cierre recibido, cerrando servidor.\n")
                        sys.stdout.flush()
                        conn.sendall(b"Servidor cerrando...")
                        return
                    if os.path.isfile(filepath):
                        with open(filepath, 'rb') as file:
                            content = file.read()
                        conn.sendall(content)
                    else:
                        conn.sendall(b"Error: El archivo no existe")
    finally:
        server_socket.close()
        sys.stdout = original_stdout

# Manejo de la señal SIGPIPE en sistemas Unix para evitar que se bloquee el servidor cuando el cliente cierra la conexión abruptamente
def handle_sigpipe(signal, frame):
    # Imprime los mensajes en la consola incluso si la salida estándar está redirigida
    sys.stdout.write("Señal SIGPIPE recibida\n")
    sys.stdout.flush()

signal.signal(signal.SIGPIPE, handle_sigpipe)

# Ejecuta la función principal si este script se ejecuta directamente
if __name__ == "__main__":
    main()

