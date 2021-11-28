import copy
a=[1,2,3]

print("=====赋值=====")
b=a
print(a)
print(b)
print(id(a))
print(id(b))

print("=====浅拷贝=====")
b=copy.copy(a)
print(a)
print(b)
print(id(a))
print(id(b))

print("=====深拷贝=====")
b=copy.deepcopy(a)
print(a)
print(b)
print(id(a))
print(id(b))



"""
赋值： 值相等，地址相等

copy浅拷贝：值相等，地址不相等

deepcopy深拷贝：值相等，地址不相等
"""
