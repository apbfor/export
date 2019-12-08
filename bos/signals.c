#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

volatile sig_atomic_t signal_number, counter = 3;
void handler(int signo) {
    signal_number = signo;
}
int main(int argc, char **argv) {
    ssize_t length = 128;
    const char* path = "/home/apbfor/Prog/python/DDZ/file.txt";
    FILE *file;
    char *buffer;
    if((file = fopen(path, "r")) == NULL){
        perror("can't open file\n");
        exit(1);
    }
    fgets(buffer, length, file);
    printf("\n%s", buffer); 
    if((fclose(file)) != 0){
        perror("error on closing file");
        exit(1);
    }
    sigset_t set;
    struct sigaction act;
    sigemptyset(&set);
    sigaddset(&set, SIGINT);
    sigprocmask(SIG_BLOCK, &set, NULL);
    act.sa_mask = set;
    act.sa_handler = handler;
    act.sa_flags = 0;
    sigaction(SIGINT, &act, NULL);
    sigemptyset(&set);
    printf("my pid %d\n", getpid());
    while(counter--){
        sigsuspend(&set);
        if (errno != EINTR) {
            perror("error on sigsuspend");
            exit(EXIT_FAILURE);
        }
        if((file = fopen(path, "r")) == NULL){
        perror("can't open file\n");
        exit(1);
        }
        fgets(buffer, length, file);
        printf("\n%s", buffer); 
        if((fclose(file)) != 0) {
            perror("error on closing file");
            exit(1);
        }
    }
    exit(EXIT_SUCCESS);
}
