import copy
a=(1,2,3)

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


#一句话就是，不可变类型，不管是深拷贝还是浅拷贝，地址值和拷贝后的值都是一样的。
