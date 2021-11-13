#include"stdio.h"

int main(int argc, char const *argv[])
{
    char *arr = "1234\0";
    scanf("%s", arr);
    printf("%s", arr);
    return 0;
}
