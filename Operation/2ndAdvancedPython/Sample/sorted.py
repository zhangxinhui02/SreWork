def process(ele):
    return ele[0]

rows = [("adam",90),("tom",80),("bob",70)]

my_sorted = sorted(rows,key=process)
print(my_sorted)

# lambda表达式的形式更为简洁
my_sorted = sorted(rows,key=lambda ele:ele[0])
print(my_sorted)
