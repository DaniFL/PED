import socket
import sqlite3
import select
import sys

class ServidorNoticias:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.clientes = {}
        self.running = True
        self.inicializar_base_datos()

    def inicializar_base_datos(self):
        self.conexion = sqlite3.connect('noticias.db', check_same_thread=False)
        self.cursor = self.conexion.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS noticias (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                autor TEXT NOT NULL,
                                titular TEXT NOT NULL,
                                contenido TEXT NOT NULL
                            )''')
        self.conexion.commit()

    def start(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        print(f"Servidor iniciado en {self.host}:{self.port}, esperando conexiones...\n")

        inputs = [self.socket_servidor, sys.stdin]

        while self.running:
            readable, _, _ = select.select(inputs, [], [])
            for s in readable:
                if s == self.socket_servidor:
                    cliente, addr = self.socket_servidor.accept()
                    print(f"\nConexión aceptada de {addr}")
                    inputs.append(cliente)
                    self.clientes[cliente] = addr
                elif s == sys.stdin:
                    comando = sys.stdin.readline().strip()
                    if comando.lower() == 'exit':
                        self.shutdown_server()
                else:
                    self.manejar_cliente(s, inputs)

    def manejar_cliente(self, socket_cliente, inputs):
        try:
            datos = socket_cliente.recv(8192).decode()  # Cambiado a 8192
            if not datos:
                raise ConnectionResetError
            print(f"Datos recibidos: {datos}")
            if datos.startswith("publicar:"):
                self.publicar_noticia(datos)
            elif datos.startswith("modificar:"):
                self.modificar_noticia(datos)
            elif datos == "solicitar_titulares":
                self.enviar_titulares(socket_cliente)
            elif datos == "listar_todos_titulares":
                self.listar_todos_titulares(socket_cliente)
            elif datos.startswith("leer_noticia:"):
                self.enviar_noticia_completa(datos, socket_cliente)
            elif datos == "menu":
                self.enviar_menu(socket_cliente)
            else:  # Asumimos que este es el nombre de usuario
                self.enviar_menu(socket_cliente)
        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Conexión con {self.clientes[socket_cliente]} cerrada. Vuelva pronto.")
            inputs.remove(socket_cliente)
            del self.clientes[socket_cliente]
            socket_cliente.close()

    def publicar_noticia(self, datos):
        _, titular, contenido = datos.split(":", 2)
        self.cursor.execute("INSERT INTO noticias (autor, titular, contenido) VALUES (?, ?, ?)", ("Autor", titular, contenido))
        self.conexion.commit()
        self.broadcast(f"Noticia publicada: {titular}")

    def modificar_noticia(self, datos):
        _, titular, contenido_adicional = datos.split(":", 2)
        self.cursor.execute("UPDATE noticias SET contenido = contenido || ? WHERE titular = ?", ("\n" + contenido_adicional, titular))
        self.conexion.commit()
        self.broadcast(f"Noticia modificada: {titular}")

    def enviar_titulares(self, socket_cliente):
        self.cursor.execute("SELECT titular FROM noticias")
        titulares = [row[0] for row in self.cursor.fetchall()]
        respuesta = "titulares:" + ":".join(titulares)
        socket_cliente.send(respuesta.encode())

    def listar_todos_titulares(self, socket_cliente):
        self.cursor.execute("SELECT titular FROM noticias")
        todos_titulares = [row[0] for row in self.cursor.fetchall()]
        respuesta = "\n".join(todos_titulares)
        socket_cliente.send(respuesta.encode())

    def enviar_noticia_completa(self, datos, socket_cliente):
        _, titular = datos.split(":", 1)
        self.cursor.execute("SELECT contenido FROM noticias WHERE titular = ?", (titular,))
        resultado = self.cursor.fetchone()
        if resultado:
            contenido = resultado[0]
            respuesta = f"contenido:{contenido}"
        else:
            respuesta = "contenido:No se encontró la noticia solicitada."
        socket_cliente.send(respuesta.encode())

    def enviar_menu(self, socket_cliente):
        menu = "\n1. Publicar nueva noticia\n2. Añadir contenido a una noticia existente\n3. Listar todos los titulares\n4. Leer contenido de una noticia\n5. Salir\n"
        socket_cliente.send(menu.encode())

    def broadcast(self, mensaje):
        mensaje_salto = "\n\n" + mensaje
        for cliente in self.clientes.keys():
            try:
                cliente.send(mensaje_salto.encode())
            except:
                pass

    def shutdown_server(self):
        print("Cerrando el servidor...")
        self.running = False
        for cliente in self.clientes.keys():
            cliente.close()
        self.socket_servidor.close()
        self.conexion.close()

if __name__ == '__main__':
    servidor = ServidorNoticias()
    servidor.start()

