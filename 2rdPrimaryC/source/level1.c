#include <stdio.h>

int main(){
    int a, b, c;
    printf("����a b c��������ֵ��������ֵ��\n");
    scanf("%d %d %d", &a, &b, &c);

    int max = a;
    if(b > max)
        max = b;
    if(c > max)
        max = c;
    
    printf("���ֵΪ��%d\n", max);

    return 0;
}