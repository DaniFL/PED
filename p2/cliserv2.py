import os
import time
import sys

def servidor(pipe_out):
    now = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    os.write(pipe_out[1], (now + "\n").encode('utf8'))
    os.close(pipe_out[1])

def cliente(pipe_in):
    data = os.read(pipe_in, 1024).decode('utf8')
    sys.stderr.write("Cliente recibe: " + data.strip() + "\n")

rd, wd = os.pipe()

pid = os.fork()

if pid:  # Proceso padre (servidor)
    os.close(rd)  # Cerramos el extremo de lectura del pipe en el servidor
    servidor((rd, wd))
else:  # Proceso hijo (cliente)
    os.close(wd)
    cliente(rd)
    os.close(rd)

