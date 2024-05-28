#include <iostream>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <cstring>
using namespace std;

int main()
{
    // Create the named pipe
    mkfifo("mypipe", 0666);

    // Open the pipe for reading
    int fd = open("mypipe", O_RDONLY);
    if (fd == -1)
    {
        perror("open");
        exit(1);
    }

    // Read the time string from the pipe
    char buffer[256];
    int bytesRead = read(fd, buffer, sizeof(buffer));
    if (bytesRead == -1)
    {
        perror("read");
        exit(1);
    }

    // Close the pipe
    close(fd);

    // Print the time string to the console
    cout << buffer << endl;

    return 0;
}
