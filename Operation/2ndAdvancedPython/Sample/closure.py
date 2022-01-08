def my_closure(myfun):
    def myjudge(*args):
        print("条件判断代码")
        return myfun(*args)
    return myjudge

def myfun():
    print("我的函数")

new_fun = my_closure(myfun)
new_fun()