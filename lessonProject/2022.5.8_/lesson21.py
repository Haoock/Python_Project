# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/7/23 08:08
# @Function:
import turtle
import random


def homework1():
    n = int(input())
    total_sum = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            total_sum += 1 / i
    else:
        for i in range(1, n + 1, 2):
            total_sum += 1 / i
    print("%.2f" % total_sum)


# homework1()

def homework2():
    str1 = input()
    str2 = input()
    if str1.find(str2, 0) != -1:
        print("Y")
    else:
        print("N")
    print(str1.index(str2))  # index找不到会报错，find不会


# homework2()

def practise2():
    turtle.screensize(800, 600, 'white')
    turtle.pensize(2)
    color = ['blue', 'red', 'yellow', 'pink']
    cnt = 0
    for i in range(100, 10, -10):
        turtle.fillcolor(color[random.randint(0, 3)])
        cnt += 1
        turtle.begin_fill()
        # turtle.color(color[cnt])
        turtle.circle(i)
        turtle.end_fill()
        turtle.left(90)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        turtle.right(90)
    turtle.exitonclick()


# practise2()

def practise3():
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


# practise3()

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


practise4()

# 汉诺塔问题
def move(n, A, B, C):
    if n == 1:
        print("从 %s 柱子移动到 %s 柱子" % (A, C))
        return
    move(n - 1, A, C, B)
    move(1, A, B, C)
    move(n - 1, B, A, C)


# move(3, "A", "B", "C")


# 八皇后问题：目标是为了计算总共有多少种放置的方法
Queen = [[0 for i in range(8)] for i in range(8)]
total_num = 0


def checkPos(row, col):
    # 检查行
    for i in range(8):
        if Queen[row][i] == 1:
            return False
    # 检查列
    for i in range(8):
        if Queen[i][col] == 1:
            return False
    # 检查主对角线
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if Queen[i][j] == 1:
            return False
    # 检查副对角线
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, 8)):
        if Queen[i][j] == 1:
            return False
    return True


def eightQueen(row):
    if row > 7:  # 如果八个皇后全部放完则输出
        global total_num
        total_num += 1
        print_Queen()
        return
    # 每次进入函数都需要扫描当前行的所有列，看看哪些位置是可以放皇后的
    for j in range(8):
        if checkPos(row, j):
            Queen[row][j] = 1
            eightQueen(row + 1)
            Queen[row][j] = 0


def print_Queen():
    for i in range(8):
        for j in range(8):
            if Queen[i][j] == 1:
                print('☆ ' * j + '★ ' + '☆ ' * (7 - j))
    print("*" * 20)


# eightQueen(0)
# print(total_num)




