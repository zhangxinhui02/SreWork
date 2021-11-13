#include"stdio.h"

struct seeME
{
    int a;
    char b;
};


int main(int argc, char const *argv[])
{
    struct seeME me;
    printf("The bytes the b memner holds is : %d \n", sizeof(me.b));
    printf("The bytes the a memner holds is : %d \n", sizeof(me.a));
    printf("The bytes struct holds is : %d \n", sizeof(me));
    if (sizeof(me)== (sizeof(me.a)+sizeof(me.b)))
    {
        printf("is equal");
    }else{
        printf("no no no..");
    }

    return 0;
}
