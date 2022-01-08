import time



# 定义一个函数大家来思考一下如何实现
def wrapper(func):
    start = time.time()
    res = func()
    end = time.time()
    print(f"{end - start}s")
    return res
# 使用
# res = wrapper(myfun)
# print(res)

# 我们不想改变函数的名字
# 装饰器的定义 
def timer(func): # 其参数意义为什么?
    def wrapper(*args,**kwargs): # 其参数意义为什么?
        start = time.time()
        res = func(*args,**kwargs) # 注意自行了解一下传入参数中*的含义和用法
        end = time.time()
        print(f"{end - start}s")
        return res
    return wrapper


# 我们已经写好的功能函数
@timer
def myfun(x):
    time.sleep(1)
    print(x)
    return "hhh"

# 拿到装饰好的函数
# myfun = timer(myfun)  
# 以后的使用
myfun(1) 
