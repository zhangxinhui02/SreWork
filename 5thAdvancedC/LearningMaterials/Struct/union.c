#include"stdio.h"


typedef union colors
{
    int a;
    char b;
}colors;

// struct test
// {
//     int len;
//     int high;
//     char color;
//     char *author;
// };

typedef union Goods{
    struct {
        int len;
        int high;
    }Size;

    struct {
        int R;
        int G;
        int B;
    }Colors;


    struct {
        int age;
        int high;
        char name[20];
        char nationality[20];
    }Author;

}Goods;

int main(int argc, char const *argv[])
{
    // colors s;
    // s.a = 10;
    // s.b = 'a';

    // printf("%c \n", s);
    // printf("%d", sizeof(s));

    Goods book;
    // Goods shirt;
    book.Author.high = 10;
    printf("%d", book.Size.high);

    return 0;
}
