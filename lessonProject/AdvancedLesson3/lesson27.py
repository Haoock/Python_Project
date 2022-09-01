# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/4/16 9:54 上午
# @Function:
import math


def last_homework1():
    for i in range(1, 1001):
        str_i = str(i)
        if str_i.find("3") != -1:
            if str_i.find("33") != -1:
                print("&", end="")
            print(str_i, end="")
            flag = True
            for x in range(2, i):
                if i % x == 0:
                    flag = False
            if flag:
                print("*")
            else:
                print()


last_homework1()


def last_homework2():
    lst = [1, 3, 5, 8]
    count = 0
    for i in lst:
        for j in lst:
            for k in lst:
                num = i * 100 + j * 10 + k
                if i != j and i != k and j != k:
                    count += 1
                    print(num)
    print(count)


# last_homework2()

# 关于回文数：lesson25种讲解了判断，自行完成完整的题目

# 关于寻找"lanqiao"字样的个数，回忆lesson26使用函数的做法
# 下面是不使用函数的做法
def last_homework5():
    str = input()
    str = str.lower()
    str_len = len(str)
    count = 0
    i = 0
    while i < str_len:
        if i + 6 < str_len and str[i] == 'l' and str[i + 1] == 'a' and str[i + 2] == 'n' and str[i + 3] == 'q' and str[
            i + 4] == 'i' and \
                str[i + 5] == 'a' and str[i + 6] == 'o':
            count += 1
            i = i + 5
        i += 1
    print(count)


# last_homework5()

# 求一组数据中的平均数、中位数以及众数
def algorithm_practise1():
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
    sum_num = 0
    for i in range(num_len):
        sum_num += num_tup[i]
        if max_appearance == num_tup[i]:
            max_appearance_num += 1
        else:
            max_appearance_num = 1
            max_appearance = num_tup[i]
    print("%.2f" % (sum_num / num_len))
    print("%.2f" % mid_num)
    print(max_appearance)


# algorithm_practise1()





# algorithm_practise2()

# algorithm_practise3()
# def algorithm_practise3_way2():
