#include"stdio.h"
#include"windows.h"
void story(int Depth)
{
    printf("从前有座山,里面有个老和尚给小和尚讲故事:\n");
    printf("第%d个老和尚讲的故事是:\n\n ",Depth);
    Sleep(1000);
    if (Depth == 10)
        return;
    else
    {

        Depth += 1;
        story(Depth);
    }
}

int main(int argc, char const *argv[])
{
    story(0);
    return 0;
}
