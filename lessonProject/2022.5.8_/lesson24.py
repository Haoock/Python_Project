# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/8/13 16:56
# @Function:

import turtle


def last_homework1():
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


# last_homework1()

def last_homework2():
    turtle.screensize(800, 600)
    turtle.setup(900, 700)
    turtle.speed(10)
    turtle.pencolor('yellow')
    turtle.left(36)
    for i in range(10):
        turtle.right(36)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.fillcolor("green")
        turtle.begin_fill()
        for x in range(5):
            turtle.forward(50)
            turtle.right(180 - 36)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0, 0)
    turtle.exitonclick()


# last_homework2()

def last_homework3():
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


# last_homework3()

def last_homework4():
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


# last_homework4()

# 关于chr和ord函数的使用回顾
def last_homework_temp():
    start = "A"
    start_idx = ord(start)
    for x in range(start_idx + 3, start_idx + 29):
        # print()
        print(chr(start_idx + (x - start_idx) % 26), end=" ")


# last_homework_temp()





# algorithm_practise1()




# algorithm_practise2()


# import turtle as t
# t.pencolor('yellow')
# t.fillcolor('green')
# t.speed(10)
# for i in range(20):
#     t.penup()
#     t.right(45)
#     t.forward(200)
#     t.pendown()
#     t.begin_fill()
#     t.forward(50)
#     t.left(215)
#     t.forward(50)
#     t.left(215)
#     t.forward(50)
#     t.left(215)
#     t.forward(50)
#     t.left(215)
#     t.forward(50)
#     t.end_fill()
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
# t.exitonclick()

# a = list(eval(input('')))
# b = ''
# print(len(a))
# print(min(a))
#
# # 少排序
# for i in range(len(a)):
#     b += str(a[i])
#     if i < len(a)-2:
#         b += ','
# print(b)
# c = ''
#
# # j是下标
# for j in range(len(a)):
#     if j < 27:
#         j += 64
#         c += chr(j)
#     else:
#         c += '[bad]'
# print(c)

# import time
#
#
# def sumOf2(n):
#     # 系统运行该程序的开始时间
#     start = time.time()
#
#     # 程序主体
#     # theSum = 0
#     # for i in range(1, n + 1):
#     #     for i in range(1, n + 1):
#     #         theSum += 1
#     theSum = (n * (n + 1) / 2)
#     # 系统运行该程序的结束时间
#     end = time.time()
#     return theSum, end - start
#
#
# for i in range(5):
#     print("sum is %d required % 10.7f seconds" % sumOf2(100))
# 0.0003281
# 0.0017610
# 0.0289800
# 2.8586092

# 100:   0.0000010
# 1000:  0.0000007  0.0000000
# 10000: 0.0000012

str1 = "heart"
str2 = "earthh"
str2 = list(str2)
found = True
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            str2[j] = None
            break
for k in range(len(str2)):
    if str2[k] != None:
        found = False
        print("False")
if found:
    print("True")




