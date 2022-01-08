from time import struct_time


class People(object):
    count = 0
    def __init__(self,name,sex,height):
        self.name = name
        self.sex = sex
        self.__height = height
        # People.count += 1
    def eat(self):
        print("这是People的吃饭")
        print(f"{self.name} is eating")
    def __len__(self):
        return self.__height
    
class Student(People):
    def __init__(self, name, sex, height,score):
        super().__init__(name,sex,height)  # 调用父类的构造函数
        self.score = score
    
    def eat(self):
        print("这是Student的吃饭")
        print(f"{self.name} is eating")

    def __str__(self):
        return "stu"
class Teacher(People):
    def __init__(self, name, sex, height,salary):
        super().__init__(name, sex, height)
        self.salary = salary

    def eat(self):
        print("这是Teacher的吃饭")
        print(f"{self.name} is eating")

# 构造对象
stu = Student("Lihua","man",180,90)
# print(stu.name)
stu.eat()
print(stu)
# print(hasattr(stu, 'eat'))
# print(dir(stu))
# teacher = Teacher("Zhangsan","women",180)
# print(People.count)
# teacher.eat()
# print(dir(stu))
# 属性判断
