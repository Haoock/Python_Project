# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/7 11:20 上午
# @Function:

#  80 85 83 89 98 75 80 90 78 65
def last_homework2():
    str_temp = input()
    lst = str_temp.split(" ")
    lst = [int(x) for x in lst]
    lst.sort()
    lst.pop(0)
    lst.pop(len(lst) - 1)
    print(sum(lst) / len(lst))


# last_homework2()

def algorithm_practise1():
    a = 2.0
    b = 1.0
    s = 0
    for n in range(1, 21):
        s += a / b
        t = a
        print("%d/%d" % (a + b, t))
        a = a + b
        b = t
    print(s)


# algorithm_practise1()

# 9,12,15,22,5,21,214
def algorithm_practise2():
    string = input()
    num_lst = list(eval(string))
    print(len(num_lst))
    num_list_sort = sorted(num_lst, reverse=True)
    print(num_list_sort[len(num_lst) - 1])
    for i in range(len(num_list_sort)):
        if i != len(num_list_sort) - 1:
            print(num_list_sort[i], end=",")
        else:
            print(num_list_sort[i])
    a = 'a'
    lst = []
    for x in range(ord(a), ord(a) + 26):
        # print(chr(x))
        lst.append(chr(x))
    for i in num_lst:
        if i > 26:
            print("[bad]", end="")
        else:
            print(lst[i - 1].upper(), end="")


def algorithm_practise3():
    a = 'A'
    print(chr(ord(a) + 3))
    return


def algorithm_practise5():
    n = int(input("n = "))
    lst = []
    for i in range(n + 1):
        binary = bin(i)
        lst.append(binary.count('1'))
    print(lst)


# algorithm_practise5()


# lst = [1, 2, 3, 4, 5]
# lst = []
# for i in range(1, 6):
#     lst.append(i)
# print(lst)

# 列表生成式
# lst = list(range(1, 6))
# print(lst)

# lst = [x*x for x in range(1, 6)]
# print(lst)
# lst = [1, 4, 9, 16, 25]

# x = input()
# lst = x.split(" ")
# print(lst)
# lst = [int(x) for x in lst]
# print(lst)
# lst = eval(input())
# print(lst)
#
# x = 12
# print("final score = %4d" % x)

# a = 2
# b = 1
# print("%d/%d" % (a, b))
# for i in range(20):
#     t = a
#     print("%d/%d" % (a + b, a))
#     a = a + b  # 3
#     b = t


def practise():
    lst = list(eval(input("请输入n个数字，以逗号分隔：")))
    lst2 = lst[:]
    print(len(lst))
    lst.sort(reverse=True)
    print(lst[-1])
    # for x in lst:
    #     print(x, end=",")
    for i in range(len(lst)):
        if i == len(lst) - 1:
            print(lst[i])
        else:
            print(lst[i], end=",")

    # 第一种思路：做列表
    # lst2 = ['A', 'B', 'C']
    # n = 1
    # print(lst2[n - 1])
    # 第二种思路如下所示：
    # char：表示一个字符
    print(lst2)
    flag = False
    for n in lst2:
        if n > 26 or n < 1:
            flag = True
            continue
        x = ord('A')  # 65
        res = chr(x - 1 + n)
        print(res, end="")
    if flag:
        print("[bad]", end="")

practise()

