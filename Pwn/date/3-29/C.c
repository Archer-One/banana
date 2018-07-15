#include<stdio.h>
#include<stdlib.h>
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
void calc(unsigned int n);
int main() {
	char buf[8];
	init();
    system("echo '说出来你可能不信，这是我写的计算器呢！'");
	system("echo '请先输入一个正整数n，表示要计算的数据组数：'");
    read(0,buf,6);
	calc(atoi(buf));
	puts("白~~");
	return 0;
}
void PrintMenu() {
	puts("choose an action:");
	puts("1 Add");
	puts("2 Sub");
	puts("3 Mul");
	puts("4 Div");
	puts("5 Save the result");
}
unsigned int Add()
{
	int x, y, result;
	printf("input the integer x:");
	scanf("%u", &x);
	printf("input the integer y:");
	scanf("%u", &y);
	result = x+y;
	printf("the result is %d\n", result);
	return result;
}
unsigned int Sub()
{
	int x, y, result;
	printf("input the integer x:");
	scanf("%u", &x);
	printf("input the integer y:");
	scanf("%u", &y);
	result = x - y;
	printf("the result is %d\n", result);
	return result;
}
unsigned int Mul()
{
	int x, y, result;
	printf("input the integer x:");
	scanf("%u", &x);
	printf("input the integer y:");
	scanf("%u", &y);
	result = x * y;
	printf("the result is %d\n", result);
	return result;
}
unsigned int Div()
{
	int x, y, result;
	printf("input the integer x:");
	scanf("%u", &x);
	printf("input the integer y:");
	scanf("%u", &y);
	result = x / y;
	printf("the result is %d\n", result);
	return result;
}
void calc(unsigned int n) {
	if (n>100)
		return;
	unsigned int buf[50];
	unsigned int* tmpResult = (unsigned int*)malloc(sizeof(unsigned int)*n);
	int opt;
	for (int i = 0; i<n; i++) {
		PrintMenu();
		scanf("%d", &opt);
		switch (opt) {
		case 1:
			tmpResult[i] = Add();
			break;
		case 2:
			tmpResult[i] = Sub();
			break;
		case 3:
			tmpResult[i] = Mul();
			break;
		case 4:
			tmpResult[i] = Div();
			break;
		case 5:
			memcpy(&buf, tmpResult, 4 * n);
			free(tmpResult);
			return ;
		default:
			puts("错误的输入");
		}
	}
}
