#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void B(){
    char buf[88];
    fgets(buf,sizeof(buf),stdin);
    printf(buf);
    _exit(0);
}
void A(){
    B();
}
int main(){
    setvbuf(stdout,0,_IONBF,0);
    alarm(180);
    A();
    return 0;
}