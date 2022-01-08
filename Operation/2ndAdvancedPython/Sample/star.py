def test_star(*args):
    print(args)     # 以元组的形式接收不定长参数
    print(*args)    
    x = (4,3,2,1)

test_star(1,2,3,0)

def test_stars(**kwargs):
    print(kwargs)  # 以字典形式接收了不定长的命名参数

test_stars(a=1,b=2)
