#include"stdio.h"
void fact(int n,int a ){
    static int sum = 1;
    if (n>1){
        printf("This is the %dth call fun___", a-n+1);
        printf("And n now is %d \n", n);
        fact(n - 1, a);
        sum *= n;
        printf("sum is %d\n", sum);
    }
    // n == a ? printf("%d=%d", n, sum) : printf("%d*", n);
}

int main(){
    fact(5,5);
}