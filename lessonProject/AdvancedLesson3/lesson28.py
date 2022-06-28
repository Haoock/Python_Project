# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/1 10:07 上午
# @Function:
import turtle


def last_Homework1():
    num_lst = list(eval(input()))
    total = 0
    for i in range(0, int(len(num_lst)) - 1):
        a = int(num_lst[i])
        b = int(num_lst[i + 1])
        if a * b < 0:
            # 上楼
            if b - a >= 1:
                total += (b - a - 1) * 1
            # 下楼
            elif b - a < 0:
                total += (a - b - 1) * 0.3
        else:
            # 上楼
            if b - a >= 1:
                total += (b - a) * 1
            # 下楼
            elif b - a < 0:
                total += (a - b) * 0.3
    print(total)


# last_Homework1()
def last_Homework2():
    str = input()
    res = int(input())
    nums = eval(str)
    count = 0
    for i in range(len(nums)):  # 这边不能用for x in nums原因
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == res:
                count += 1
                break
    print(count)


# last_Homework2()


# 求一组数据中的平均数、中位数以及众数
def last_Homework3():
    string = input()
    num_tup = list(eval(string))
    num_tup.sort()
    num_len = len(num_tup)
    if num_len % 2 == 0:  # 说明长度为偶数，那么中位数一定是中间两个
        mid_index_low = int(num_len / 2 - 1)
        mid_num = (num_tup[mid_index_low] + num_tup[mid_index_low + 1]) / 2
    else:
        mid_index_low = int((num_len + 1) / 2)  # 否则是中间那一个
        mid_num = num_tup[mid_index_low]
    max_appearance_num = -1  # 众数出现的最多次数
    max_appearance = -1  # 众数
    max_appearance_num_temp = -1
    max_appearance_temp = -1
    sum_num = 0
    for i in range(num_len):
        sum_num += num_tup[i]
        if max_appearance_temp == num_tup[i]:
            max_appearance_num_temp += 1
            if max_appearance_num_temp > max_appearance_num:
                max_appearance_num = max_appearance_num_temp
                max_appearance = max_appearance_temp
        else:
            max_appearance_num_temp = 1
            max_appearance_temp = num_tup[i]
    print("%.2f" % (sum_num / num_len))
    print("%.2f" % mid_num)
    print(max_appearance)


# last_Homework3()

def algorithm_practise1():
    a = 2.0
    b = 1.0
    s = 0
    for n in range(1, 21):
        s += a / b
        t = a
        a = a + b
        b = t
    print(s)


# algorithm_practise1()

# 9,12,15,22,5,21,214
def algorithm_practise3():
    string = input()
    num_lst = list(eval(string))
    print(len(num_lst))
    num_list_sort = sorted(num_lst, reverse=True)
    print(num_list_sort[len(num_lst) - 1])
    for i in range(len(num_list_sort)):
        if i != len(num_list_sort) - 1:
            print(num_list_sort[i], end=",")
        else:
            print(num_list_sort[i])
    a = 'a'
    lst = []
    for x in range(ord(a), ord(a) + 26):
        # print(chr(x))
        lst.append(chr(x))
    for i in num_lst:
        if i > 26:
            print("[bad]", end="")
        else:
            print(lst[i - 1].upper(), end="")


# algorithm_practise3()

def algorithm_practise4():
    colors = ['black', 'red', 'yellow']
    turtle.screensize(800, 600, 'white')
    for i in range(3):
        turtle.pencolor(colors[i])
        turtle.fillcolor(colors[i])
        turtle.begin_fill()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
        turtle.right(180)
        turtle.forward(20)
        turtle.left(90)
    turtle.exitonclick()


# algorithm_practise4()


# [1,3,3,5,5,7,9,9]
# lst = list(eval(input()))
# count_max = 0  # 众数数量
# common_val = 0  # 众数
# lst.sort()  # 原地操作
# for i in range(1, len(lst)):
#     if lst[i] == lst[i - 1]:
#         continue
#     else:
#         count = lst.count(lst[i])
#         if count >= count_max:
#             common_val = lst[i]
#             count_max = count
# print(common_val)



# for x in lst:
#     x = lst.count(3)
#     if x =














