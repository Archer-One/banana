#include<stdio.h>
#include<string.h>
void input(){
	char l[100];
	read(0,l,300);
}
int main(){
	char *a = "就是一道pwn题，让你一眼能看出漏洞那种，本题提供 /bin/sh";
	char buf[100];
	write(1,a,strlen(a));
	input();
	return 0;
}
