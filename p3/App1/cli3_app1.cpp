#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string>

using namespace std;

int main()
{
    const char *pipe_name = "mypipe";

    // Asegurar que el named pipe existe
    if (mkfifo(pipe_name, 0666) == -1 && errno != EEXIST)
    {
        perror("mkfifo");
        return 1;
    }

    while (true)
    {
        int fd = open(pipe_name, O_WRONLY);
        if (fd == -1)
        {
            perror("open pipe");
            return 1;
        }

        string filename;
        cerr << "Introduce el nombre del fichero o escribe 'salir' para terminar: ";
        getline(cin, filename);

        if (filename == "salir")
        {
            write(fd, filename.c_str(), filename.size() + 1);
            close(fd);
            break;
        }

        // Enviar el nombre del archivo al servidor
        write(fd, filename.c_str(), filename.size() + 1);
        close(fd);

        // Leer la respuesta del servidor
        fd = open(pipe_name, O_RDONLY);
        if (fd == -1)
        {
            perror("open pipe for reading");
            return 1;
        }

        char buffer[1024];
        ssize_t bytes_read = read(fd, buffer, sizeof(buffer));
        if (bytes_read > 0)
        {
            buffer[bytes_read] = '\0';
            string response(buffer);
            if (response == "no encontrado")
            {
                cerr << "El archivo " << filename << " no fue encontrado." << endl;
            }
            else
            {
                cerr << "Contenido del archivo " << filename << ":\n" << response << endl;
            }
        }

        close(fd);
    }

    return 0;
}

