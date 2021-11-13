#include"stdio.h"
#include"string.h"
struct Box
{
    int length;
    int height;
    char color[20];
};
typedef struct Box Box;

typedef struct Boox{
    int length;
    int height;
    char color[20];

} Boox;

void setLen(Box *box,int len){
    box->length = len;
}

void setHeight(Box *box,int height){
    box->height = height;
}

int main(int argc, char const *argv[])
{
    struct Box  black = {100,100,"black"};
    black.length = 1;
    black.height = 1;
    strcpy(black.color, "red");
    printf("The color is %s , the len = %d , the height = %d \n",
           black.color,
           black.height,
           black.length);

    struct Box * T=&black;
    printf("%d   ", T->length);
    printf("%d", black.length);
    // setLen(&black, 10);
    // setHeight(&black, 100);
    // printf("The len is %d and The height is %d", black.height, black.length);

    // struct Box boxT;
    // Box boxP;
    return 0;
}
