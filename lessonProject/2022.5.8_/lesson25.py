# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/8/20 10:16
# @Function:
import turtle
import math


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
    a = 2  # a是分子
    b = 1  # b是分母
    s = 0
    for n in range(1, 21):
        # s += a / b
        t = a  # 先记录分子a的值
        a = a + b  # 每次循环让a（分子）更新为a + b
        b = t  # 每次循环让b（分母）变成a
        print("%d/%d" % (a, b))  # 输出分子/ 分母
    print(s)


# last_homework2()

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
    nums = list(eval(input()))
    target = int(input())  # 目标值
    flag = False
    lst = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                lst.append(i)
                lst.append(j)
                flag = True
                break
        if flag:
            break
    print(lst)


# last_homework4_way1()


def last_homework4_way2():
    nums = list(eval(input()))
    target = int(input())  # 目标值
    flag = False
    lst = []
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        if nums[p1] + nums[p2] > target:
            p2 -= 1
        elif nums[p1] + nums[p2] < target:
            p1 += 1
        else:
            lst.append(p1)
            lst.append(p2)
            break
    print(lst)


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
    m = int(input())  # 输入第一个数字
    n = int(input())  # 输入第二个数字
    maxn = 1000001  # 最大的素数范围
    p = [False] * maxn  # p数组专门用于表示第i个数字是否是素数，如果为素数，那么是False，否则是True
    prime = []  # prime列表专门用于存储所有的素数
    for i in range(2, maxn, 1):  # 开始筛选素数（埃式筛法）
        if not p[i]:  # 如果i是素数
            prime.append(i)
            if len(prime) == n:  # 如果找了n个素数，那么就停止寻找
                break
            for j in range(i * 2, maxn, i): # 开始将素数的倍数筛去
                p[j] = True
    count_num = 0  # 用来计数
    for i in range(m, n + 1):
        print(prime[i - 1], end=" ")
        count_num += 1
        if count_num % 10 == 0:
            print()

algorithm_practise2()


def is_Prime(x):
    # 输入一个数字
    # 输出这个数字是否是素数，
    # 如果是素数：True
    # 如果不是素数：False
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True


def find_Prime():
    lst = []
    for i in range(101, 201):
        if is_Prime(i):
            lst.append(i)
    print(lst)

# find_Prime()

class Stack():
    def __init__(self):
        self.items = []

    # 将一个元素添加到栈顶
    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop(len(self.items) - 1)
        return self.items[len(self.items) - 1]

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        if len(self.items) != 0:
            return False
        else:
            return True

    def size(self):
        return len(self.items)



