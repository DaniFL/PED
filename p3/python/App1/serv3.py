import os

def create_fifo(path):
    if os.path.exists(path):
        os.unlink(path)
    os.mkfifo(path)

def main():
    fifo_in_path = "/tmp/fifo_cli3_to_serv3"
    fifo_out_path = "/tmp/fifo_serv3_to_cli3"

    # Crear o recrear FIFOs
    create_fifo(fifo_in_path)
    create_fifo(fifo_out_path)

    print("Servidor en funcionamiento. Esperando datos del cliente...")

    while True:
        with open(fifo_in_path, 'r') as fifo_in:
            filepath = fifo_in.read().strip()
            if filepath == "exit":
                print("Terminando el servidor.")
                break
            if not filepath:
                continue

            try:
                with open(filepath, 'r') as file:
                    content = file.read()
            except FileNotFoundError:
                content = "Error: File not found."

            with open(fifo_out_path, 'w') as fifo_out:
                fifo_out.write(content)

if __name__ == "__main__":
    main()

