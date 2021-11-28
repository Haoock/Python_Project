s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)  #求交集他们是等价的

print(s1.union(s2))
print(s1 | s2)  #求并集他们是等价的

#下面是求差集
print(s1.difference(s2))
print(s1 - s2)
print(s2 - s1)

#对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
