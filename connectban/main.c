#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

// Configuration
#define PORT 22

int main (int argc, char *argv[]){
    //fork();
    fprintf(stderr, "Started connect-ban\n");

    // Make socket
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);

    if (sockfd == -1){
        perror("Creation failed");
        exit(1);
    }

    // Create listen socket
    struct sockaddr_in localaddress;
    localaddress.sin_family = AF_INET;
    localaddress.sin_addr.s_addr = INADDR_ANY;
    localaddress.sin_port = htons(PORT);

    // Bind the socket to the address
    if (bind(sockfd, (struct sockaddr *)&localaddress, sizeof(localaddress)) == -1){
        perror("Bind error");
        exit(1);
    }

    // Listen
    if (listen(sockfd, 50) == -1) {
        perror("Listen error");
        exit(1);
    }

    struct sockaddr_in remoteaddress;
    int addr_length = sizeof(remoteaddress);

    for(;;) {
        fprintf(stderr, "Listening \n");
        int remotefd;

        if((remotefd = accept(sockfd, (struct sockaddr *) &remoteaddress, (socklen_t *) &addr_length)) == -1){
            perror("Accept error");
            exit(1);
        }
        fprintf(stderr, "Get R3KT %s \n", inet_ntoa(remoteaddress.sin_addr));
        
        char command[2048] = "iptables -I ssh-filter 1 -s ";
        strcat(command, inet_ntoa(remoteaddress.sin_addr));
        strcat(command, " -j DROP");
        //printf(command);
        system(command);

        close(remotefd);

    }
    //int returncode = system("echo test");
}
