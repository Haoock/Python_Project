# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/8/20 10:16
# @Function:
import turtle


# 求选手的得分平均值
def last_homework1():
    str_temp = input()
    lst = str_temp.split(" ")
    lst = [int(x) for x in lst]
    lst.sort()
    lst.pop(0)
    lst.pop(len(lst) - 1)
    print(sum(lst) / len(lst))


def last_homework2():
    a = 2.0
    b = 1.0
    s = 0
    for n in range(1, 21):
        s += a / b
        t = a
        a = a + b
        b = t
    print(s)


# 绘制四个小五角星
def draw(x, y, d):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(d)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(20)
        turtle.right(144)
    turtle.end_fill()


def last_homework3():
    # 国旗的四边
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.color('red', 'red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(438)
        turtle.right(90)
        turtle.forward(292)
        turtle.right(90)
    turtle.end_fill()
    # 绘制大五角星
    turtle.color('yellow', 'yellow')
    turtle.penup()
    turtle.goto(-170, 145)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(50)
        turtle.right(144)

    turtle.end_fill()

    draw(-100, 180, 305)
    draw(-85, 150, 30)
    draw(-85, 120, 3)
    draw(-100, 100, 300)
    turtle.hideturtle()
    turtle.done()

def last_homework4_way1():
    nums = eval(input())
    target = int(input())


# def last_homework4_way2():

def algorithm_practise1():
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


# 数素数
def algorithm_practise2():
    m = int(input())
    n = int(input())
    maxn = 1000001
    p = [False] * maxn
    prime = []
    for i in range(2, maxn, 1):
        if p[i] == False:
            prime.append(i)
            if len(prime) == n:
                break
            for j in range(i + i, maxn, i):
                p[j] = True
    count_num = 0
    for i in range(m, n + 1):
        print(prime[i - 1], end=" ")
        count_num += 1
        if count_num % 10 == 0:
            print()


