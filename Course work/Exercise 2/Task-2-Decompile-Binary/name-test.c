#include <stdio.h>
#include <stdlib.h>

int main(){
    char name[32];

    printf("Enter your name: ");
    fgets(name, 32, stdin);
    printf("Hello, ");
    printf("%s", name);
    putchar(10);
    return 0;
}
