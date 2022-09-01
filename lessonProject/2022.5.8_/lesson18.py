# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/7/2 09:53
# @Function:
import turtle as t


#
def homework(str1, str2, arr):
    if str1 == "插入排序":
        insertionSort(arr, str2)
    if str1 == "选择排序":
        selectionSort(arr, str2)

def compare(num1, num2, para):
    if para == "升序":
        return num1 < num2
    if para == "降序":
        return num1 > num2


def insertionSort(arr, str):
    # 假设现在需要从小到大进行排序
    # 第0位前面没有数字，因此我们假设已经排好，不予考虑，因此从第一位开始循环
    for i in range(1, len(arr)):
        index = i - 1
        now_num = arr[i]
        while index >= 0:
            # arr[index]只有两种可能性，一种是>now_num，一种是<= now_num
            # if arr[index] < now_num:    # 只要比now_num小，就交换，然后一直往前找，一直找到比now_num大的则停止，这是
            if compare(arr[index], now_num, str):
                arr[index + 1] = arr[index]
            else:
                break
            index -= 1
        arr[index + 1] = now_num


def selectionSort(arr, str):
    # 每次选择最小的数排列到最前面
    for i in range(len(arr)):
        min_num_index = i  # 每次假设当前i处的数字最小
        for j in range(i + 1, len(arr)):
            # if arr[j] < arr[min_num_index]: # 每次将最小的数字放到当前的位置
            if compare(arr[min_num_index], arr[j], str):
                min_num_index = j
        arr[i], arr[min_num_index] = arr[min_num_index], arr[i]  # 将最小的数组放到当前的位置


# arr = [12, 11, 13, 5, 6]
# selectionSort(arr, "降序")
# print("排序后的数组是：")
# for i in range(len(arr)):
#     print(arr[i], end=" ")


# 下面是浩轩的作业：
# 评价：暴力解法，没有体现出任何编码的技巧。还会报错
def homework(aee, a, b):
    if a == 1 and b == 1:
        for i in range(len(aee)):
            pre_index = i - 1
            now_value = aee[i]
            while pre_index >= 0:
                if aee[pre_index] > now_value:
                    aee[pre_index + 1] = aee[pre_index]
                else:
                    break
                pre_index -= 1
            aee[pre_index + 1] = now_value
    if a == 1 and b == 1:
        for i in range(len(aee)):
            min_num_index = i
            for j in range(i + 1, len(aee)):
                if aee[j] > aee[min_num_index]:
                    min_num_index = j
            aee[i], aee[min_num_index] = aee[min_num_index], aee[i]
    if a == 1 and b == 2:
        for i in range(len(aee)):
            pre_index = i - 1
            now_value = aee[i]
            while pre_index >= 0:
                if aee[pre_index] < now_value:
                    aee[pre_index + 1] = aee[pre_index]
                else:
                    break
                pre_index -= 1
            aee[pre_index + 1] = now_value
    if a == 2 and b == 2:
        for i in range(len(aee)):
            min_num_index = i
            for j in range(i + 1, len(aee)):
                if aee[j] > aee[min_num_index]:
                    min_num_index = j
            aee[i], aee[min_num_index] = aee[min_num_index], aee[i]


# aee = [12, 11, 13, 5, 6]
# homework(aee,a=1,b=1)
# for x in aee:
#     print(x, end=' ')


def binarySearch(arr, num):
    # if arr[0] > arr[1]:
    #     arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return False


# arr = [2, 4, 6, 8, 10, 15, 16]
# arr2 = [15, 13, 12, 10, 9, 8, 4]
# res = binarySearch(arr2, 9)
# print(res)

def bubbleSort(arr):
    # 冒泡排序（从小到大排列）一般是将最大的冒泡到最后面，或者是将最小的冒泡到最前面。
    # 这里选择将最大数冒泡到最后
    # i是每一轮遍历
    sum1 = 0
    for i in range(len(arr) - 1, 0, -1):
        flag = False
        # j是每一次交换
        for j in range(1, i + 1):
            # 如果i号位置的元素比j号位置的元素大，则交换
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = True
                sum1 += 1
        # flag为False的时候说明没有产生交换
        if not flag:
            break
    return sum1


arr = [12, 11, 13, 5, 6]
print(bubbleSort(arr))
print("排序后的数组是：")
for i in range(len(arr)):
    print(arr[i], end=" ")


def binarySearch(arr, num):
    # 二分查找一定对数组的顺序敏感
    # 如果是降序，转成升序
    if arr[0] > arr[1]:
        arr.sort()
    low = 0
    high = len(arr) - 1
    # 范围在low和high之间
    while low <= high:
        mid = int((low + high) / 2)
        if num == arr[mid]:
            # 找到num元素返回True
            return True
        elif num < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # 没有找到num元素返回False
    return False


# arr = [1, 3, 2, 5, 7, 9, 10]
# print(arr)
# arr2 = [11, 9, 7, 5, 4, 2]
# print(binarySearch(arr2, 4))


#
# t.circle(80)
# 设置画布大小和颜色
# t.screensize(800, 600, "green")
# 设置窗口大小
# t.setup(1000, 600)
# 将turtle暂停，鼠标点击的时候会退出
# t.exitonclick()
