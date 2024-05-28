#include <iostream>
#include <ctime>
#include <unistd.h>
#include <iomanip>
#include <fcntl.h>
#include <sys/stat.h>
#include <cstring>

using namespace std;

int main()
{
    // Create the named pipe
    mkfifo("mypipe", 0666);

    // Open the pipe for reading and writing
    int fd = open("mypipe", O_RDWR);
    if (fd == -1)
    {
        perror("open");
        exit(1);
    }

    while (true)
    {
        // Get the current time
        time_t rawtime;
        time(&rawtime);

        // Convert the time to a string
        tm *timeinfo = localtime(&rawtime);
        char buffer[256];
        strftime(buffer, sizeof(buffer), "%c", timeinfo);

        // Write the time string to the pipe
        int bytesWritten = write(fd, buffer, strlen(buffer) + 1);
        if (bytesWritten == -1)
        {
            perror("write");
            exit(1);
        }

        // Wait for a new client
        sleep(1);
    }

    return 0;
}
