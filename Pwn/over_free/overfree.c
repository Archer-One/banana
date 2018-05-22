#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
char *cmd;
void sh(char *c)
{system(c);}
int main()
{
char *ptr[8];
int size,n;
setvbuf(stdout,0,_IONBF,0);
memset(ptr,0,sizeof(ptr));
cmd=malloc(128);
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
	else if (!strncmp(cmd,"remove",6))
	{
		printf("Index: ");
		scanf("%d%*c",&n);
		if(n>=0&&n<8&&ptr[n])
		{
		puts(ptr[n]);
		free(ptr[n]);
		ptr[n]=0;
		}
		else
		{
		puts("Nothing here");
		}

	}
	else {puts("unknow command");}
}

return 0;

}

