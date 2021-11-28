import copy
l=[1,2,3,[4, 5]]

l1=l #赋值
l2=copy.copy(l) #浅拷贝
l3=copy.deepcopy(l) #深拷贝
l.append(6)

print(l)  # [1,2,3,[4,5],6]
print(l1) # [1,2,3,[4,5],6]
print(l2) # [1,2,3,[4,5]]
print(l3) # [1,2,3,[4,5]]
