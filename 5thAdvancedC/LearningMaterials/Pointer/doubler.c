#include"stdio.h"
#include"stdlib.h"
// void doubler(int a ){
//     a = a + a;
// }

int compare(const void *a ,const void *b){
    return *(int *)a - *(int *)b;
}

int main(int argc, char const *argv[])
{
    // int x = 10;
    // doubler(x);
    // printf("X value is %d", x);
    // return 0;
    int arr[10] = {7, 2, 1, 6, 3};
    qsort(arr, 5, sizeof(int), compare);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", arr[i]);
    }

}
