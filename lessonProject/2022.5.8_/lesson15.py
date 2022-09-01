# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/11 09:49
# @Function:

def sanjiao(a, b, c):
    try:
        if a + b > c and a + c > b and b + c > a:
            print(a, b, c)
        else:
            raise ValueError("不能构成三角形！")
    except ValueError as e:
        print("引发异常：", e)

# sanjiao(3, 4, 10)


def Algorithm_Practise1():
    for i in range(1, 8, 2):
        for j in range(1, i + 1):
            print("*",end="")
        print("\n")

# Algorithm_Practise1()

# lst = list(eval(input()))
# lst.sort(reverse=False)
# for x in lst:
#     print(x, end=" ")

# a = 0
# for i in range(1, 101):
#     a += i

# print(int(111))
m = int(input())
n = int(input())
lst = []
for i in range(m, n+1):
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)
for i in range(len(lst)):
    if i == len(lst) - 1:
        print(lst[i])
    else:
        print(lst[i],end=",")