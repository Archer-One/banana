#include <stdio.h>
int test()
{
char a,b,c,d,e,f,g=102;
    scanf("%s",&g);//bug
    printf("%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g);
    return 0;
}
int main(void){
    test();
}
