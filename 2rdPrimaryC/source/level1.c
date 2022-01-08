#include <stdio.h>

int main(){
    int a, b, c;
    printf("输入a b c三个数的值，输出最大值：\n");
    scanf("%d %d %d", &a, &b, &c);

    int max = a;
    if(b > max)
        max = b;
    if(c > max)
        max = c;
    
    printf("最大值为：%d\n", max);

    return 0;
}