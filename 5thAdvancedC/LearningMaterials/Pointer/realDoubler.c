#include"stdio.h"

// void fake_doubler(int *x){
//     x = x + (unsigned long long)x;
// }

void real_doubler(int *x){
    *x = *x + *x;
}
int main(int argc, char const *argv[])
{
    int a=1;
    int *p =  &a;
    real_doubler(&a);
    printf("%d", a);
    return 0;
}
