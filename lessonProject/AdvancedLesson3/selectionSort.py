# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/3/5 3:45 下午
# @Function:
# 选择排序

def selectionSort(arr):
    # 每次选择最小的数排列到最前面
    for i in range(len(arr)):
        min_num_index = i  # 每次假设当前i处的数字最小
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_num_index]:
                min_num_index = j
        arr[i], arr[min_num_index] = arr[min_num_index], arr[i]  # 将最小的数组放到当前的位置


arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("排序后的数组是：")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')

"""
    for i in range(len(arr)):
        min_num_index = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min_num_index]:
                min_num_index = j
            j += 1
        temp = arr[i]
        arr[i] = arr[min_num_index]
        arr[min_num_index] = temp
"""
