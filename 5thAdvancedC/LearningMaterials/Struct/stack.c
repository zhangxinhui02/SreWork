#include"stdio.h"
#include"malloc.h"



typedef int ElementType;
typedef struct Node{
    ElementType var;
    struct Node *next;
} Node;

typedef struct Stack{
    Node * base;   //! EBP为栈底指针
    Node * top;   //! ESP 为栈顶指针
}Stack;

void initStack(struct Stack * T){
    T->base = (Node*)malloc(sizeof(Node));
    //! 动态分配

    // memory alloc 分配内存
    //! 在堆上申请一块内存
    //! malloc(arg) arg = 你要分配内存的大小
    //! void* = 分配内存首地址
    T->base->var = 100;
    T->top = T->base;
}

void pushStack(int var,struct Stack *T){
    Node *tmp = malloc(sizeof(Node));
    tmp->next = T->top;
    T->top = tmp;
    T->top->var = var;
}

int popStack(struct Stack *T){
    Node *tmp = T->top;
    int e = T->top->var;
    T->top = T->top->next;
    free(tmp);
    return e;
}
int a;
int main(int argc, char const *argv[])
{
    // Node A;
    // Node B;
    // A.next = malloc(sizeof(Node));
    // A.next->var = 10;
    // printf("%d", A.next->var);

    Stack test;
    initStack(&test);
    pushStack(1, &test);
    pushStack(2, &test);
    pushStack(3, &test);
    Node A;
    test.base = malloc(sizeof(Node));

    for (int i = 0; i < 3; i++)
    {
        printf("The %dth pop :%d\n", i, popStack(&test));
    }


    return 0;
}
