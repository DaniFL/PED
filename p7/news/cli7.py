import socket
import sys

class ClienteNoticias:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket_cliente = None

    def start(self, nombre=None):
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_cliente.connect((self.host, self.port))
        self.nombre = nombre if nombre is not None else input("Introduce tu nombre de usuario: ")
        self.socket_cliente.send(self.nombre.encode())
        self.mostrar_menu()

    def enviar_articulo(self):
        try:
            while True:
                opcion = input("Elige una opción del 1-5: ")
                if opcion == '1':
                    titular = input("Escribe el titular de la noticia: ")
                    cuerpo = input("Escribe el cuerpo de la noticia: ")
                    noticia = f"publicar:{titular}:{cuerpo}"
                    self.socket_cliente.send(noticia.encode())
                elif opcion == '2':
                    self.socket_cliente.send("solicitar_titulares".encode())
                    respuesta = self.socket_cliente.recv(8192).decode()
                    _, titulares = respuesta.split(':', 1)
                    if titulares.strip():
                        sys.stderr.write("Titulares disponibles para modificar:\n")
                        for titulo in titulares.split(':'):
                            sys.stderr.write(titulo + "\n")
                        titular = input("Escribe el titular de la noticia a modificar: ")
                        contenido_adicional = input("Escribe el contenido adicional para la noticia: ")
                        noticia = f"modificar:{titular}:{contenido_adicional}"
                        self.socket_cliente.send(noticia.encode())
                    else:
                        sys.stderr.write("No hay titulares disponibles para modificar.\n")
                        continue
                elif opcion == '3':
                    self.socket_cliente.send("listar_todos_titulares".encode())
                    respuesta = self.socket_cliente.recv(8192).decode()
                    if respuesta.strip():
                        sys.stderr.write("Titulares disponibles:\n")
                        sys.stderr.write(respuesta + "\n")
                    else:
                        sys.stderr.write("Actualmente no hay titulares disponibles.\n")
                elif opcion == '4':
                    self.socket_cliente.send("listar_todos_titulares".encode())
                    respuesta = self.socket_cliente.recv(8192).decode()
                    if respuesta.strip():
                        sys.stderr.write("Titulares disponibles:\n")
                        sys.stderr.write(respuesta + "\n")
                        titular = input("Escribe el titular de la noticia que deseas leer: ")
                        self.socket_cliente.send(f"leer_noticia:{titular}".encode())
                        contenido = self.socket_cliente.recv(8192).decode()
                        if "contenido:" in contenido:
                            _, noticia = contenido.split(":", 1)
                            sys.stderr.write(noticia + "\n")
                        else:
                            sys.stderr.write("Error: No se pudo leer el contenido de la noticia.\n")
                    else:
                        sys.stderr.write("Actualmente no hay titulares disponibles.\n")
                elif opcion == '5':
                    self.desconectar()
                    break
                else:
                    sys.stderr.write("Opción inválida. Por favor, elige una opción válida.\n")
                    self.mostrar_menu()
        except KeyboardInterrupt:
            sys.stderr.write("Interrupción de teclado\n")
        finally:
            self.desconectar()

    def mostrar_menu(self):
        self.socket_cliente.send("menu".encode())
        menu = self.socket_cliente.recv(8192).decode()
        sys.stderr.write(menu + "\n")

    def desconectar(self):
        sys.stderr.write("Desconectando...\n")
        self.socket_cliente.close()

if __name__ == '__main__':
    cliente = ClienteNoticias()
    cliente.start()
    cliente.enviar_articulo()

