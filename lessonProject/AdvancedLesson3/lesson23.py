# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/3/20 上午
# @Function:

# homework1：求第10次反弹多高，以及初始落下到第10次反弹到最高点时一共经过多少米

# def homework1(n):
#     max_height = n  # 每次最高点的高度
#     res = 0     # 总路程
#     for i in range(10):
#         res += max_height + max_height / 2
#         max_height /= 2
#     print(max_height)
#     print(res)
#
#
# homework1(20)


# def selectionSort(arr):
#     # 每次选择最小的数排列到最前面
#     for i in range(len(arr)):
#         min_num_index = i  # 每次假设当前i处的数字最小
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_num_index]:
#                 min_num_index = j
#         arr[i], arr[min_num_index] = arr[min_num_index], arr[i]  # 将最小的数组放到当前的位置
#
# # 可以有两种方法,另一种方法是利用之前学习的排序算法
#
# def homework2(lst):
#     lst.sort()
#     print(lst)
#     i = lst[0]
#     for x in lst:
#         if x != i:
#             print(i)
#             break
#         i += 1
#
#
# lst = input().split(',')
# print(lst)
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# print(lst)
# homework2(lst)


# str = input()
# lst = str.split(',')
# lst = lst[:-1]
# for i in lst:
#     print(i, end=" ")

# def homework3(str1, str2, arr):
#     if str1 == "插入排序":
#         insertion_sort2(arr, str2)
#     if str1 == "选择排序":
#         selection_sort2(arr, str2)
#
#
# def compare(num1, num2, para):
#     if para == "升序":
#         return num1 < num2
#     if para == "降序":
#         return num1 > num2
#
#
# def insertionSort1(arr):
#     length = len(arr)  # 数组的长度
#     for i in range(1, length):
#         current = arr[i]
#         pre_index = i - 1
#         while pre_index >= 0 and arr[pre_index] < current:
#             arr[pre_index + 1] = arr[pre_index]
#             pre_index -= 1
#         arr[pre_index + 1] = current
#
#
# def insertion_sort2(arr, str):
#     length = len(arr)  # 数组的长度
#     for i in range(1, length):
#         current = arr[i]
#         pre_index = i - 1
#         while pre_index >= 0 and compare(current, arr[pre_index], str):
#             arr[pre_index + 1] = arr[pre_index]
#             pre_index -= 1
#         arr[pre_index + 1] = current
#
#
# def selectionSort(arr):
#     # 每次选择最小的数排列到最前面
#     for i in range(len(arr)):
#         min_num_index = i  # 每次假设当前i处的数字最小
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_num_index]:
#                 min_num_index = j
#         arr[i], arr[min_num_index] = arr[min_num_index], arr[i]  # 将最小的数组放到当前的位置
#
#
# def selection_sort2(arr, str):
#     # 每次选择最小的数排列到最前面
#     for i in range(len(arr)):
#         min_num_index = i  # 每次假设当前i处的数字最小
#         for j in range(i + 1, len(arr)):
#             if compare(arr[j], arr[min_num_index], str):
#                 min_num_index = j
#         arr[i], arr[min_num_index] = arr[min_num_index], arr[i]  # 将最小的数组放到当前的位置
#
#
# def bubbleSort(arr):
#     # 每次将大的数字冒泡到最后面
#     for i in range(len(arr) - 1, 0, -1):
#         j = 1
#         while j <= i:
#             if arr[j] > arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j += 1
#
#
# arr = [64, 25, 12, 22, 11]
# insertionSort1(arr)
# homework3("选择排序", "降序", arr)
# print(arr)

# algorithm practise3

# str.find(str, beg=0, end=len(string))
str1 = input()
str2 = input()
# if str1.find(str2, 3) != -1:
#     print("Y")
# else:
#     print("N")

lst = list(str1)
flag = False # 标志
for x in lst:
    if x == str2:
        flag = True
        break
if not flag:
    print("N")
if flag:
    print("Y")

n = int(input())
total_num = 1
num = 1
for i in range(2, n + 1):
    num = num + i
    total_num += num
print(total_num)

