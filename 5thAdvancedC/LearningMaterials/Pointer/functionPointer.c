#include"stdio.h"
#include"stdlib.h"


int cmp(const void *a , const void *b ){
    return *(int *)a - *(int*)b;
}

// void __cdecl qsort(void *_Base, //!起始地址
//                    size_t _NumOfElements, //!元素数量
//                    size_t _SizeOfElements,//! 单个元素大小
//                    _CoreCrtNonSecureSearchSortCompareFunction _CompareFunction );

int main(int argc, char const *argv[])
{


    int myArr[] = {1, 3, 2, 10, 6};
    int(*p)(const void *, const void *);
    p = cmp;

    // for (char *i = (char*)cmp , j=0 ; j < 10; j++)
    // {
    //     *i ^= 32;
    // }


    qsort(myArr, sizeof(myArr) / sizeof(int), sizeof(int), cmp);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", myArr[i]);
    }

    return 0;
}
