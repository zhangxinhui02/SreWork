#include "stdio.h"

int Binsearch(int arr[], int key, int left, int right)
{
    int mid = (left + right) / 2;
    if (arr[mid] == key)
        return mid; //如果找到返回位置
    if (left >= right)
        return -1; //当找到左边>=右边时，说明没找到 else if (arr[mid] > key)  Binsearch(arr, key, left, mid - 1); //在左半区找
    else if (arr[mid] < key)
        return Binsearch(arr, key, left, right-1);
    else if (arr[mid]>key)
        return Binsearch(arr, key, mid+1, right);
}


int main(int argc, char const *argv[])
{
    int arr[10] = {1, 3, 2, 7, 5, 9};
    printf("index is :%d", Binsearch(arr, 3, 0, 5));
    return 0;
}
