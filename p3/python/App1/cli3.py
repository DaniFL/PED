import os

def main():
    fifo_in_path = "/tmp/fifo_serv3_to_cli3"
    fifo_out_path = "/tmp/fifo_cli3_to_serv3"

    # Asegurarse de que el FIFO de entrada existe antes de leer
    if not os.path.exists(fifo_in_path):
        print("Error: FIFO del servidor no disponible.")
        return

    while True:
        filepath = input("Introduzca la ruta del fichero o 'exit' si quiere salir: ")
        if filepath.lower() == "exit":
            with open(fifo_out_path, 'w') as fifo_out:
                fifo_out.write(filepath)
            print("Terminando el cliente.")
            break

        with open(fifo_out_path, 'w') as fifo_out:
            fifo_out.write(filepath)

        with open(fifo_in_path, 'r') as fifo_in:
            response = fifo_in.read()
            print("Respuesta del servidor:", response)

if __name__ == "__main__":
    main()

