#include"stdio.h"

int main(int argc, char const *argv[])
{
    void *t;
    int int_var[2]={0,1};
    char char_var[2]={'a','b'};
    double double_var[2]={1.1,2.2};

    int *p = int_var;
    printf("%x  ", (p + 1));
    printf("%x", p);

    return 0;
}
