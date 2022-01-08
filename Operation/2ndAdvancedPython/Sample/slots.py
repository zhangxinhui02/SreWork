class People():
    __slots__ = ("name","age")
    def __init__(self,name):
        self.name = name
        # self.score = 99  # 这里直接报错AttributeError: 'People' object has no attribute 'score'

peo = People("zhangsan")
print(peo.name)
print(peo.score)