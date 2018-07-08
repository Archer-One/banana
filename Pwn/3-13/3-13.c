#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
void A()
{
	setvbuf(stdout, 0, _IONBF, 0);
	srand(time(0) ^ getpid());
	char buf[100];
	int magic = rand();
	gets(buf);
	if (atoi(buf) == magic) {
		puts("Okay...");
		system("sh");
	}
}
int main(){
	A();
}
0xffffcedc magic
0xffffce78 buf






