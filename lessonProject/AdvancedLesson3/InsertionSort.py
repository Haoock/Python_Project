# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/2/27 2:27 下午
# @Function:

def insertionSort(arr):
    length = len(arr)  # 数组的长度
    for i in range(1, length):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current

        # for j in range(i - 1, -1, -1):
        #     if arr[j] >= temp:
        #         arr[j + 1] = arr[j]
        #     else:
        #         res = j
        #         break
        # arr[res] = temp


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("排序后的数组是：")
for i in range(len(arr)):
    print(arr[i])
