# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/3/5 4:04 下午
# @Function:
def bubbleSort(arr):
    # 从后往前进行比较
    for i in range(len(arr)-1, 0, -1):
        j = 1
        while j <= i:
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j += 1
    return


arr = [11, 12, 10, 13, 9, 8]
bubbleSort(arr)
print("排序后的数组是：")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')

"""
    # 从后往前进行比较
    for i in range(len(arr)):
        j = len(arr) - 1
        flag = False
        while j > i:
            if arr[j] < arr[j - 1]:
                flag = True
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            j -= 1
        if not flag:
            break
"""
