# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/18 13:37
# @Function:

def lastHomework():
    lst = list(eval(input()))
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                if i != j and i != k and j != k:
                    print(lst[i], lst[j], lst[k])


# lastHomework()
# 8, 4: 4, 0
# 4, 8: 8, 4
# 9, 6: 6, 3 : 3, 0
# 这是使用递归的方法来做
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


# 下面是一般的方法：
def gcd2(m, n):
    min_num = min(m, n)
    for x in range(min_num, 0, -1):
        if m % x == 0 and n % x == 0:
            return x


# print(gcd2(20,10))
# BE QUITE!
# EXPERIENCE IS THE BEST TEACHER.
# JULY,DO YOU KNOW? FAITH CAN MOVE MOUNTAINS.
# IT'S AMAZING!
def review7():
    # 初始化
    dic = {}
    max_num = -1  # 记录出现字母的最多的次数，这个例子中是字母E
    for i in range(26):
        dic[chr(ord('A') + i)] = 0
    for i in range(4):
        str = input()
        for x in str:
            if 'A' <= x <= 'Z':
                dic[x] += 1
                if dic[x] > max_num:
                    max_num = dic[x]

    # 先来正着输出一遍
    for i in range(max_num + 1):
        if i == 0: # 第一行比较特殊
            for j in range(26):
                if j == 0:
                    print(chr(ord('A') + j), end="")
                else:
                    print(" " + chr(ord('A') + j), end="")
        else: # 剩下的行数就直接按照dic中的数字输出就好了
            print("\n", end="")
            zero_num = 0
            for j in range(26):
                if j == 0 and dic[chr(ord('A') + j)] != 0:
                    dic[chr(ord('A') + j)] -= 1
                    print("*", end="")
                elif j == 0 and dic[chr(ord('A') + j)] == 0:
                    zero_num += 1
                elif j != 0 and dic[chr(ord('A') + j)] == 0:
                    zero_num += 2
                elif j != 0 and dic[chr(ord('A') + j)] != 0:
                    dic[chr(ord('A') + j)] -= 1
                    print(" " * zero_num, end="")
                    print(" *", end="")
                    zero_num = 0



# review7()

lst = list(eval(input()))
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i != j and i != k and j != k:
                print("%d,%d,%d" %(lst[i], lst[j], lst[k]))
