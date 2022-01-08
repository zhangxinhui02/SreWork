# 位置参数
def fun1(a,b): # fun(1,2),也可以fun(a=1,b=2)
    pass

# 当写一个*,后面的参数必须命名传递
def keyword_only(*,kw1):
    print(kw1)

# keyword_only(kw1 = 4)

# 可变长度的参数
def len_changeable(*args):
    print(args) # 以元组形式传递
    print(*args) # 解包
# len_changeable(1,2,3,4)

x=10
def default(a=x):
    print(a)
    print(locals()) # 使用globals可以打印全局的名称空间
x=100
default()
