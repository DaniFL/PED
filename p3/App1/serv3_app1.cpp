#include <iostream>
#include <fstream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string>
#include <cstring>

using namespace std;

int main()
{
    const char *pipe_name = "mypipe";
    char buffer[1024];

    // Crear el named pipe si no existe
    if (mkfifo(pipe_name, 0666) == -1 && errno != EEXIST)
    {
        perror("mkfifo");
        return 1;
    }

    while (true)
    {
        int fd = open(pipe_name, O_RDONLY);
        if (fd == -1)
        {
            perror("open pipe for reading");
            return 1;
        }

        // Leer el nombre del archivo desde el pipe
        ssize_t bytes_read = read(fd, buffer, sizeof(buffer));
        if (bytes_read > 0)
        {
            buffer[bytes_read] = '\0';
        }
        else
        {
            close(fd);
            continue;
        }

        string filename(buffer);
        if (filename == "salir")
        {
            close(fd);
            break;
        }

        close(fd);

        // Verificar si el archivo existe
        ifstream file(filename);
        if (file.is_open())
        {
            string content((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
            file.close();

            // Enviar el contenido del archivo al cliente
            fd = open(pipe_name, O_WRONLY);
            if (fd == -1)
            {
                perror("open pipe for writing");
                return 1;
            }
            write(fd, content.c_str(), content.size() + 1);
            close(fd);
        }
        else
        {
            // Enviar mensaje de que el archivo no se encontró
            fd = open(pipe_name, O_WRONLY);
            if (fd == -1)
            {
                perror("open pipe for writing");
                return 1;
            }
            string not_found_msg = "no encontrado";
            write(fd, not_found_msg.c_str(), not_found_msg.size() + 1);
            close(fd);
        }
    }

    cout << "Servidor desconectado" << endl;

    return 0;
}

