import socket
import sys

def prompt(message):
    print(message, file=sys.stderr)
    return input()

def main():
    original_stdin = sys.stdin

    host = prompt("Ingrese la dirección IP del servidor: ")
    port = int(prompt("Ingrese el puerto del servidor (debe coincidir con el del servidor): "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except Exception as e:
        print(f"No se pudo conectar con el servidor: {str(e)}", file=sys.stderr)
        return

    while True:
        try:
            filepath = prompt("Ingrese la ruta completa del archivo a enviar o 'exit' para salir: ")
            if filepath.lower() == 'exit':
                break
            client_socket.sendall(filepath.encode())
            response = client_socket.recv(1024)
            print("Respuesta recibida del servidor:", file=sys.stderr)
            print(response.decode(), file=sys.stdout)
        except Exception as e:
            print(f"Error durante la comunicación con el servidor: {str(e)}", file=sys.stderr)
            break

    client_socket.close()
    sys.stdin = original_stdin

if __name__ == "__main__":
    main()

