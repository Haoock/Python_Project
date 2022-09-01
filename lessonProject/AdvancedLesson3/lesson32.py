# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/28 15:42
# @Function:

def sqrt(x):
    for i in range(x):
        if i * i > x:
            return i - 1


# print(sqrt(9))

def binary_search(nums, target):
    # nums是已经排好序的列表数组 1, 2, 3, 4, 5, 6
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


def isStraight(nums):
    repeat = set()  # {     }
    ma, mi = 0, 14
    for num in nums:
        if num == 0:
            continue  # 跳过大小王
        ma = max(ma, num)  # 最大牌
        mi = min(mi, num)  # 最小牌
        if num in repeat: return False  # 若有重复，提前返回 false
        repeat.add(num)  # 添加牌至 Set
    return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


def str_con(s, n):
    a = s[n:]
    b = s[:n]
    return a + b  # 字符串用加号拼接


# s = input("输入s")
# n = int(input("输入n"))
# res = str_con(s, n)
# print(res)

def my_sqrt(x):
    res = -1
    for i in range(x):
        if i * i > x:
            res = i
            break
    return res - 1


# x = int(input())
# r = my_sqrt(x)
# if r == -1:
#     print("你的函数输出错误")
# else:
#     print(r)


# 0 7 8 10 11

# 0 0 5 7 10

class BBQ:
    name = "野外烧烤"  # 类属性
    people_num = "5人"

    def __init__(self, name):
        print("我和", name, "去吃BBQ")

a1 = BBQ("小雨，小靖")
a2 = BBQ("小雨辰，小靖哲")
print(BBQ.name)
print(BBQ.people_num)
BBQ.people_num = "3人"
print(a1.people_num)
print(a2.people_num)
a1.people_num = "8人"
print(a1.people_num)
print(a2.people_num)
