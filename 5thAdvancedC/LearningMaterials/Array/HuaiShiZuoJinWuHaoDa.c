#include"stdio.h"

int main(int argc, char const *argv[])
{
    char name[] = "HuaiShiZuoJinWuHaoDa";
    for (int i = 0; i < sizeof(name)/sizeof(char); i++)
    {
        printf("%c", name[i]);
    }
    
    return 0;
}
