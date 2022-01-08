L1 = [1,2,3]
L2 = L1
# 猜猜结果? -> 一样
print(id(L1))
print(id(L2))

# 猜猜结果?
print(id(L1[0]))
print(id(L2[0]))
print(id(1))

# 改变一下
L1[0] = 99
# 猜猜结果?
print(id(L1))
print(id(L2))
# 猜猜结果?
print(L1)
print(L2)

l1 = [1,2,3]
def fun(lis):
	li[2] = 99

print(l1[2])