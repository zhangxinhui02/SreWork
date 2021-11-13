#include"stdio.h"

int len(char * arr){ //
    return sizeof(arr) / sizeof(char); //8
}

int main(int argc, char const *argv[])
{
    unsigned long long a;
    char arr[100];
    printf("The length in main function : %d\n", sizeof(arr) / sizeof(char));
    printf("The length in another function : %d\n", len(arr));
    return 0;
}
