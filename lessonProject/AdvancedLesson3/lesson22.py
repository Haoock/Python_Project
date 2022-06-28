# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/3/13 12:53 下午
# @Function:


# str1 = input()
# res1 = str1.split(" ")
# print(res1)
# res2 = "～"
# print(res2.join(res1))


# 计算n以内奇数的和
# n = int(input("N:为"))
# sum_num = 0
# for i in range(1, n + 1, 2):
#     sum_num += i
# print(sum_num)


# def bubbleSort(arr):
#     # 每次将大的数字冒泡到最后面
#     for i in range(len(arr) - 1, 0, -1):
#         j = 1
#         while j <= i:
#             if arr[j] > arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j += 1
#
# bubbleSort()

# N：3
#
# 0 - 3
#
# 321
# 231
# 201
# 301
#
# 123
# 213
# 203
# 103

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

#
#
# # 第一种方法
# def countNum1(N):
#     count = 0
#     for i in range(N, 0, -1):  # 百位数取不到0
#         for j in range(N, -1, -1):  # 十位数都可以取到
#             for k in range(N, -1, -1):  # 个位数也都可以取到
#                 num = i * 100 + j * 10 + k
#                 if j != i and k != j and k != i and num % 2 == 1:
#                     count += 1
#     return count
#
#
# # 第二种方法
# def countNum2(N):
#     count_odd = 0
#     for i in range(1, N + 1, 2):
#         count_odd += 1
#     total_num = count_odd * (N + 1 - 2) * (N + 1 - 2)
#     return total_num
#
#
# N = 6
# print(countNum1(N))
