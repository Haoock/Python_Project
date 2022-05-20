# -*- coding: utf-8 -*-
# @Author  : Haock
# 周末上午小班练习
# @Time    : 2022
# @Function:
import random
import os


def last_homework1_way1():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # lst = [x for x in range(1, 11)]
    # lst2 = list(range(1, 11))
    s = ['+', '-']
    file = open("text.txt", 'w')
    for i in range(10):
        a = random.choice(lst)
        b = random.choice(lst)
        if a < b:
            c = a
            a = b
            b = c
        c = random.choice(s)
        string = str(a) + c + str(b) + "=_______\n"
        file.write(string)
    file.close()


# last_homework1_way1()


def last_homework1_way2():
    s = ['+', '-']
    file = open("text.txt", 'w')
    for i in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if a < b:
            c = a
            a = b
            b = c
        c = random.choice(s)
        string = str(a) + c + str(b) + "=_______\n"
        file.write(string)
    file.close()


def last_homework1_haoxuan():
    import random
    f = open('t.txt', 'a')
    for i in range(0, 10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 3)
        if a >= b and c == 1:
            e = str(a) + "+" + str(b) + "="
            f.write(e)
            d = str(int(input('')))
            f.write(d)
            if d == (a + b):
                f.write('正确')
            if d != (a + b):
                f.write('错误')
        if a >= b and c == 3:
            f.write(a, '-', b, '=')
            d = int(input(''))
            if d == (a - b):
                f.write('正确')
            if d != (a - b):
                f.write('错误')
        if a <= b and c == 2:
            f.write(b, '-', a, '=')
            d = int(input(''))
            if d == (b - a):
                f.write('正确')
            if d != (b - a):
                f.write('错误')
    f.close()


# last_homework1_xuanhao()

def last_homework2():
    string = "If you find a path with no obstacles, it probably doesn’t lead anywhere"
    dic = {}
    f = open("t.txt", 'a')
    for x in string:
        if x in dic.keys():
            dic[x] += 1
        else:
            dic[x] = 1
    for k, v in dic.items():
        print(k, '出现了', v, '次')
        f.write(k + " " + str(v) + '\n')
    f.close()


# last_homework2()
def last_homework2_xuanhao():
    a = 'If you find a path with no obstacles, it probably doesn’t lead anywhere'
    d = {}
    for i in a:
        str_i = str(i)
        for j in str_i:
            if j not in d.keys():
                d[j] = 1
            else:
                d[j] += 1
    for k, v in d.items():
        print(k, '出现了', v, '次')


# x1 = [1, 2, 3, 1]
# x2 = tuple(x1)  # (1, 2, 3, 1)
# x3 = list(x2)  # [1, 2, 3, 1]
# x3.remove(2)
# print(len(x3))
# print(x3)

# set           # {1, 2, 3, 1}


# x4 = {1, 2, 3, 1}
# x4.add(5)
# x4.discard(9)
# print(x4)


# x5 = set([1, 2, 3, 4])
# print(x4)
# dict          # {"A":1, "B":"1", "A": 1}
# print(x3)
# print(type(x3))


# A:2,4,6,8,9,10
# 小明：2,4,10
# 小红：4,6,8,10,12
def algorithm_practise():
    A = set(eval(input("A:")))
    ming = set(eval(input("小明：")))
    hong = set(eval(input("小红：")))
    if ming.issubset(A):
        print("小明是A组的成员")
    else:
        print("小明不是A组的成员")
    if hong.issubset(A):
        print("小红是A组的成员")
    else:
        print("小红不是A组的成员")
    print("小红和小明拥有的共同数字是：")
    print(ming.intersection(hong))


# algorithm_practise()

def temp():
    s1 = {10, 20, 30, 40}
    s2 = {20, 30, 40, 50, 60}
    print(s1.intersection(s2))
    print(s1 & s2)  # 求交集他们是等价的

    print(s1.union(s2))
    print(s1 | s2)  # 求并集他们是等价的

    # 下面是求差集
    print(s1.difference(s2))
    print(s1 - s2)
    print(s2 - s1)

    # 对称差集
    print(s1.symmetric_difference(s2))
    print(s1 ^ s2)


# homework1()


# lst = []
# for i in range(1, 101):
#     lst.append(i)
# print(lst)
#
# # 第一种列表生成式
# lst = list(range(1, 101))
# print(lst)
#
# # 第二种
# # lst = [1, 2, 3,5, 6, ..... 100]
# lst = {x for x in range(1, 101)}
# print(lst)
#
# string = 'fdsafdasdf'
# lst = list(string)
# print(lst)
#
# set1 = set(string)
# print(set1)

# x = {1, 2, 3, 4, 5}
# print(x)
# print(x)
# for i in x:
#     print(i)
#
# for k,v in range(4):
#     print(v)


# for i in range(len(x)):
#     print(x[i])
# A = {1,2,3}
# B = {1,2,3,4}
# print(A.issubset(B))
# print(B.issuperset(A))

string = input("A:")
print(type(string))
# JAVA C C++ Go python...

