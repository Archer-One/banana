#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include<signal.h>
void handler(int signum){
	puts("Timeout");
	_exit(1);
}
void init(){
	setvbuf(stdout,0,_IONBF,0);
	setvbuf(stdin,0,_IONBF,0);
	setvbuf(stderr,0,_IONBF,0);
	signal(SIGALRM,handler);
	alarm(60);
}
int main(){
    int fd;
    char buf[32];
	init();
    if((fd = open("/tmp/flag",O_RDONLY))==-1){
        puts("打开文件失败，若一段时间后重试仍然失败请联系管理员！");
        exit(-1);
    }
    char* content = malloc(sizeof(char)*100);
    read(fd,content,100);
    read(0,buf,32);
    printf(buf);            
    return 0;
}
