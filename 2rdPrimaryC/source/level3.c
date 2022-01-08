#include <stdio.h>

int main(){
    int num[3][3];

    printf("输入一个3X3的矩阵，元素之间使用空格间隔，每行之间换行：\n");

    for(int i = 0;i<3;i++){
        scanf("%d %d %d",&num[i][0],&num[i][1],&num[i][2]);
    }
    
    int result1 = num[0][0] + num[1][1] + num[2][2];
    int result2 = num[0][2] + num[1][1] + num[2][0];
    
    printf("主对角线元素和：%d\n副对角线元素和：%d\n\n",result1,result2);

    return 0;
}