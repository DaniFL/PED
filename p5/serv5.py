import socket
import sys

def servidor():
    # Solicitar el puerto al usuario
    sys.stderr.write("Ingrese el puerto en el que el servidor escuchará las solicitudes: ")
    puerto = int(input())

    # Crear un socket UDP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Vincular el socket a la dirección y puerto local
        servidor_socket.bind(("0.0.0.0", puerto))
        sys.stderr.write(f"Servidor escuchando en el puerto {puerto}\n")

        while True:
            # Recibir datos del cliente
            datos, direccion_cliente = servidor_socket.recvfrom(4096)

            # Decodificar la ruta del archivo recibida
            ruta_archivo = datos.decode()

            if ruta_archivo.lower() == 'salir':
                break

            try:
                # Leer el contenido del archivo
                with open(ruta_archivo, "r") as archivo:
                    contenido = archivo.read()
                    # Enviar el contenido del archivo al cliente
                    servidor_socket.sendto(contenido.encode(), direccion_cliente)
            except FileNotFoundError:
                # Enviar un mensaje de error si el archivo no existe
                servidor_socket.sendto("ERROR: Archivo no encontrado".encode(), direccion_cliente)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")

    finally:
        # Cerrar el socket
        servidor_socket.close()

if __name__ == "__main__":
    servidor()

