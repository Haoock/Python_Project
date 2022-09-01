# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/11
# @Function:

# 2,2,0,0,0,3,0,0,1,0
def lastHomework2():
    lst = list(map(int, input().split(" ")))
    for i in range(1, 10):
        if lst[i] > 0:
            print("%d" %i, end="")
            lst[i] -= 1
            break
    for i in range(10):
        for j in range(lst[i]):
            print(i, end="")

# lastHomework2()

def algorithm_practise1_way1(prices):
    ans = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            ans = max(ans, prices[j] - prices[i])
    return ans


def algorithm_practise1_way2(prices):
    inf = int(1e9)
    minprice = inf
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit


hashTable = [False] * 3

def generateP_way1():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and i != k:
                    print(i, j, k)
# 生成1， 2， 3的所有可能的情况第二种方法
def generateP(index):
    if index == 3:
        for i in range(3):
            print(p[i], end="")
        print()
        return
    for i in range(0, 3):
        if not hashTable[i]:
            p[index] = i
            hashTable[i] = True
            generateP(index + 1)
            hashTable[i] = False


num = [1, 2, 3]
p = [0] * 3
# generateP(0)

# generateP_way1()

def check(b, row, col):
    i = 0
    while i < row:
        if abs(col - b[i]) in (0, abs(row - i)):
            return False
        i += 1
    return True


def b_print(b):
    for col in b:
        print(' . ' * col + ' x ' + ' . ' * (len(b) - 1 - col))
    print('_' * 100)


def eight_queens(b, row):
    b_len = len(b)
    if row == b_len:
        b_print(b)
    col = 0
    while col < b_len:
        if check(b, row, col):
            b[row] = col
            eight_queens(b, row + 1)
        col += 1


#
# lst = list(map(int, input().split(" ")))
# print(lst)

# lst = list(eval(input()))
# count = 0
# for x1 in lst:
#     for x2 in lst:
#         if x2 == x1:
#             count += 1
#     if count > len(lst) / 2:
#         print(x1)
#         break
#
# lst = list(eval(input()))
# min_num = lst[0]
# min_index = 0
# for i in range(len(lst)):
#     if lst[i] < min_num:
#         min_index = i
#         min_num = lst[i]
# max_num = min_num
# max_index = min_index
# for i in range(min_index, len(lst)):
#     if lst[i] > max_num:
#         max_num = lst[i]
#         max_index = i
# print(max_num - min_num)


# dic = {"a":1, "b":2}
# for k,v in dic.items():
#     print(k, v)
# dic["a"] = 2
# print(dic)
#
# str = "123"
# str[0] = 3
# print(str)

a = ["name", "age", "sex"]
b = ["Dong", 38, "Male"]
dic = {}
for i in range(len(a)):
    dic[a[i]] = b[i]

