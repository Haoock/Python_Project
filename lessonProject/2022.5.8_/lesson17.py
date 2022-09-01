# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/24 21:30
# @Function:
# 求第10次反弹多高，以及初始落下到第10次反弹到最高点时一共经过多少米
def practise1(n):
    max_height = n  # 每次最高点的高度
    res = 0  # 总路程
    for i in range(10):
        res += max_height + max_height / 2
        max_height /= 2
    print(max_height)
    print(res)


def practise2(str_input):
    english_count = 0
    kong_count = 0
    digital_count = 0
    other_count = 0
    for x in str_input:
        if x.isalpha():
            english_count += 1
        elif x == ' ':
            kong_count += 1
        elif x.isdigit():
            digital_count += 1
        else:
            other_count += 1
    print(english_count)
    print(kong_count)
    print(digital_count)
    print(other_count)


def insertionSort(arr):
    # 假设现在需要从小到大进行排序
    # 第0位前面没有数字，因此我们假设已经排好，不予考虑，因此从第一位开始循环
    for i in range(1, len(arr)):
        index = i - 1
        now_num = arr[i]
        while index >= 0:
            # arr[index]只有两种可能性，一种是>now_num，一种是<= now_num
            if arr[index] < now_num:
                arr[index + 1] = arr[index]
            else:
                break
            index -= 1
        arr[index + 1] = now_num
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


arr = [12, 11, 13, 5, 6]


# insertionSort(arr)
# print("排序后的数组是：")
# for i in range(len(arr)):
#     print(arr[i], end=" ")

def selectionSort(arr):
    # 每次选择最小的数排列到最前面
    for i in range(len(arr)):
        min_num_index = i  # 每次假设当前i处的数字最小
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_num_index]:
                min_num_index = j
        arr[i], arr[min_num_index] = arr[min_num_index], arr[i]  # 将最小的数组放到当前的位置


def insertion1(arr):
    for i in range(1, len(arr)):
        pre_index = i - 1
        now_value = arr[i]
        while pre_index >= 0:
            if arr[pre_index] > now_value:
                arr[pre_index + 1] = arr[pre_index]
            else:
                break
            pre_index -= 1
        arr[pre_index + 1] = now_value
        print("第", i, "次循环", end="")
        print(arr)


# arr1 = [12, 11, 13, 5, 6]
# insertion1(arr1)
# for x in arr1:
#     print(x, end=" ")


def selection1(arr):
    for i in range(len(arr)):
        min_num_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_num_index]:
                min_num_index = j
        arr[i], arr[min_num_index] = arr[min_num_index], arr[i]


# arr1 = [12, 11, 13, 5, 6]
# selection1(arr1)
# for x in arr1:
#     print(x, end=" ")

a = input()
b = 0
c = 0
d = 0
for x in a:
    if x.isalpha():
        b+=1
    if x.isdigit():
        c += 1
