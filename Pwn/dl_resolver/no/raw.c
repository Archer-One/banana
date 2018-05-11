#include<stdio.h>
#include<unistd.h>
#include<string.h>
char buf[1000000];
void m()
{
char local[10];
int len=read(0,buf,sizeof(buf));
memcpy(local,buf,len);
}
int main()
{
m();
}
