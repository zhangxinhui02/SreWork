#include <stdio.h>

int main(){
    printf("输入一个数，判断是否为素数：\n");
    int num;
    scanf("%d", &num);

    if(num < 2){
        printf("Error\n");
        return 0;
    }

    for(int i = 2; i < num; i++){
        if(num % i == 0){
            printf("not prime\n");
            return 0;
        }
    }
    printf("prime");

    return 0;
}