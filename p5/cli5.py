import socket
import sys

def cliente():
    # Solicitar la dirección IP y el puerto al usuario
    sys.stderr.write("Ingrese la dirección IP del servidor: ")
    servidor_ip = input()
    sys.stderr.write("Ingrese el puerto del servidor: ")
    servidor_puerto = int(input())

    # Crear un socket UDP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Solicitar la ruta del archivo al usuario
            sys.stderr.write("Ingrese la ruta del archivo (o 'salir' para terminar): ")
            ruta_archivo = input()
            
            if ruta_archivo.lower() == 'salir':
                break

            # Enviar la ruta del archivo al servidor
            cliente_socket.sendto(ruta_archivo.encode(), (servidor_ip, servidor_puerto))

            # Recibir la respuesta del servidor
            respuesta, _ = cliente_socket.recvfrom(4096)

            # Mostrar la respuesta recibida del servidor
            sys.stderr.write("Respuesta del servidor:\n")
            sys.stderr.write(respuesta.decode() + "\n")

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")

    finally:
        # Cerrar el socket
        cliente_socket.close()

if __name__ == "__main__":
    cliente()

