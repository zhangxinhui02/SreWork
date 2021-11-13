#include"stdio.h"

int main(int argc, char const *argv[])
{

    // int a; // 4bytes
    // char b; // 1Bytes
    // char *char_p = &b;
    // printf("0x%x\n", char_p);
    // int x = char_p + 1;
    // printf("0x%x", x);
    void * x;
    int a;
    char b;
    float c;
    x = &a+1; //int  add 4
    x = &b; //char add 1
    x = &c; //float add 4

    return 0;
}
