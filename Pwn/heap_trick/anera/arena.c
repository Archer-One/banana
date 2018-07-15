#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>

void sh(char *c)
{system(c);}
char cmd[1024];
int main()
{
char *ptr[8];
char magic[32];
int size,n;
setvbuf(stdout,0,_IONBF,0);
memset(ptr,0,sizeof(ptr));
gets(magic);
while(1)
{
	fgets(cmd,128,stdin);
	if(!strncmp(cmd,"add",3))
	{
		printf("Index: ");
		scanf("%d",&n);
		if(n>=0&&n<8)
		{
		printf("Size: ");
		scanf("%d%*c",&size);
		ptr[n]=malloc(size);
		printf("Data: ");
		gets(ptr[n]);
		}
		else
		{
		puts("Out of bound");
		}
	}
	else if (!strncmp(cmd,"print",5))
	{
		printf("Index: ");
		scanf("%d",&n);
		if(n>=0&&n<8&&ptr[n])
		{
		printf("Size: ");
		scanf("%d%*c",&size);
		write(1,ptr[n],size);
		}
		else
		{
		puts("Nothing here");
		}

	}
	else if(!strncmp(cmd,"exit",4)){break;}
	else {puts("unknow command");}
}

return 0;

}

