# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/18 17:22
# @Function:

def last_homework():
    str = "This is an apple"
    index = 0
    length = len(str)
    for i in range(len(str)):
        # print(str[i])
        if str[i] == ' ':
            index += 1
        # if 'a' <= str[i] <= 'z' and 'A' <= str[i] <= 'Z':
        #     print(str[i])
        #     index += 1
    print(length - index)


# last_homework()

def practise1():
    str = "This is an apple!"
    str = str.replace("an apple", "a pear")
    print(str)


def practise2():
    N = int(input())
    # 找出组合数：能够组成3位数的组合个数
    # 利用for循环：
    countNum = 0
    for i in range(N, 0, -1):
        for j in range(N, -1, -1):
            for k in range(N, -1, -1):
                num = i * 100 + j * 10 + k
                if num % 2 != 0 and j != k and j != i and k != i:
                    countNum += 1
    print(countNum)


# practise2()




# lst = ("this", "is")
# str = " "
# str = str.join(lst)
# print(str)
# str.

# n = int(input())
# countn = 0
# for i in range(1, n + 1):
#     for j in range(n + 1):
#         for k in range(n + 1):
#             num = i * 100 + j * 10 + k
#             if i != j and i != k and j != k and num % 2 != 0:
#                 countn += 1
# print(countn)

# n = str(int(input()))
# print(len(n))
# str = n[::-1]
# print(str)

# str = "This is an apple"
# str = str.replace("an apple", "a pear")
# print(str)
#
# lst = str.split(" ")
# lst.remove(lst[2])
# lst.remove(lst[2])
# lst.append("a")
# lst.append("pear")
# str = " "
# str = str.join(lst)
# print(str)

# str = "This is an apple"
# print("%s!" % str)


