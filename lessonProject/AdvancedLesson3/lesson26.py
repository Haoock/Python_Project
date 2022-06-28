# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/4/9 上午
# @Function:
import math
import random
import turtle


def homework1():
    # 方法一：将数字逆转
    # num = int(input())
    # 方法二：直接利用字符串
    num = input()
    length = len(num)
    print(length)
    num2 = num[::-1]
    for x in num2:
        print(x)


# homework1()

def homework2():
    str = input()
    nums1 = eval(str)
    lst = list(nums1)
    # nums2 = str.split(',')
    print(nums1)
    print(lst)
    lst.sort(reverse=True)
    print(lst)
    # print(nums2)
    # nums1_res = sorted(nums1)  # 元组可以利用sorted方法
    # print(nums1_res)



    # num_list = [9, 1, 8, 2, 5, 6]  # list的sort方法与元组不同
    # num_list.sort()
    # print(num_list)


# homework2()


def homework3():
    turtle.screensize(800, 600, 'white')

    turtle.fillcolor('yellow')
    turtle.penup()
    turtle.goto(0, -50)
    turtle.forward(50)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3):
        turtle.left(90)
        turtle.forward(100)
        if i == 1:
            turtle.forward(50)
    # 开始画底部
    turtle.left(90)
    turtle.forward(10)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.forward(70)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.forward(10)
    turtle.end_fill()
    # 开始画轮胎
    turtle.left(180)
    turtle.penup()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.circle(15)
    turtle.end_fill()
    # 开始画第二个轮胎
    turtle.left(180)
    turtle.penup()
    turtle.forward(100)
    turtle.left(180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.circle(15)
    turtle.end_fill()
    turtle.exitonclick()


# homework3()

def homework4():
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


# homework4()

# 需要同学们把这道题目完成，上节课只是完成了判断的要求
# def lastPractise():

def practise1():
    str = input()
    str = str.lower()
    x = str.count("lanqiao")
    print(x)


# practise1()
def practise2():
    n = int(input())
    dic = {}
    for i in range(1, n + 1):
        dic[i] = i * i
    print(dic)

    count = 0
    for key, value in dic.items():
        print("%d:%d" % (key, value), end="")
        count += 1
        if count != n:
            print(",", end="")


practise2()

# practise3 仿照lesson22
# def practise3():


def practise4():
    turtle.screensize(800, 600)
    turtle.setup(900, 700)
    turtle.fillcolor('yellow')
    turtle.speed(7)
    for i in range(5):
        length = random.randint(10, 150)
        turtle.penup()
        turtle.goto(random.randint(-250, 250), random.randint(-150, 150))
        turtle.pendown()
        turtle.pensize(5)
        turtle.begin_fill()
        for x in range(5):
            turtle.forward(length)
            turtle.right(180 - 36)
        turtle.end_fill()
        # turtle.penup()  # 提笔，不留痕迹
        # fdx = length - (math.sqrt(5) - 1) / 2 * length
        # turtle.fd(fdx)  # 向前走76.9像素，即|2-7|的x长度
        # turtle.pd()  # 落笔，开始画线，即7点坐标位置，开始画五角星内的正五边形水平向左的边长
        # # 画内部五边形，并且填充红色
        # turtle.fillcolor("yellow")  # 填充颜色
        # turtle.begin_fill()  # 开始填充颜色
        # for i in range(5):  # 一共有5条边，画5次，5个循环
        #     turtle.fd(length - 2 * fdx)  # 第一次画，向右边长
        #     turtle.right(72)  # 转角72°
        # turtle.end_fill()  # 结束填充
    turtle.exitonclick()


# practise4()
