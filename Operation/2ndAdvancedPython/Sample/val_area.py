res = 1 
def fun1():
    res = 3 
    def fun2(): 
        print(res)
    return fun2

# 注意这里的返回值是个啥?
# fun = fun1()
# fun()

def fun3():
    res = 999
    fun2 = fun1() # 把闭包返回过来
    fun2()
    # print(locals())
fun3()

# print(globals())