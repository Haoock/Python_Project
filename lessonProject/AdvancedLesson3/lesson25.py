# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/4/2 上午
# @Function:
import random
import turtle


# 123
# 123 % 10 = 3 * 100 = 0 + 300 = 300
# 123 // 10 = 12
# 12 % 10 = 2 * 20 = 20 + 300 = 320
# 12 // 10 = 1
# 1 % 10 = 1 + 320 = 321
# 1 // 10 = 0
#
# 321
# 123456
# 654321

# 公鸡每只5元，母鸡每只3元，小鸡三只1元，用100元买100只鸡，问公鸡、母鸡、小鸡各多少只？
def homework2():
    # flag1 = False
    # flag2 = False
    M = int(input())
    num = int(input())
    gj_num = int(M / 5 + 1)
    for x in range(gj_num):
        for y in range(34):
            for z in range(301):
                total_money = 5 * x + 3 * y + z * 1 / 3
                if total_money == M and x + y + z == num:
                    print("小鸡的数量是：%d,母鸡的数量是：%d，公鸡的数量是：%d" % (z, y, x))
                    break


# homework2()

def homework3():
    turtle.pensize(2)
    for i in range(4):
        turtle.fd(100)
        turtle.circle(20, 180)
        turtle.fd(100)
        turtle.right(90)
    turtle.exitonclick()


# homework3()

# n = 123
# n_temp=123
def judge_num(n):
    # 两种做法
    # 1. 第一种做法就是将数字转成回文之后的数字
    # n_temp = n  # 123
    # z = 0  # 321
    # while n_temp != 0:  # 只有n为0的时候才会跳出该循环
    #     temp = n_temp % 10
    #     z = z * 10 + temp
    #     n_temp //= 10
    # print(z)
    # if z == n:
    #     print("yes")
    # else:
    #     print("no")
    # 2. 第二种做法是将数字转成字符串来做
    string = str(n)  # abce   ecba
    string_temp = string[::-1]
    print(string_temp)
    if string_temp == string:
        print("yes")
    else:
        print("no")


# judge_num(12320)
# homework4(12321)

#  猴子吃桃问题
def practise1():
    x = 1
    for i in range(9):
        x = (x + 1) * 2
    print(x)


# practise1()

# 关于turtle的练习题：
#
def practise2():
    turtle.screensize(800, 600, 'white')
    turtle.color('red')  # 笔的颜色
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.fillcolor('blue')
    turtle.circle(40)
    turtle.end_fill()
    turtle.exitonclick()


# practise2()

def practise_test():
    turtle.screensize(800, 600, 'white')
    turtle.pensize(2)

    for i in range(150, 50, -10):
        turtle.circle(i)
        turtle.penup()
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.pendown()
    turtle.exitonclick()

# practise_test()

def practise3():
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


# practise3()

def practise4():
    turtle.color('red')
    turtle.pensize(3)
    turtle.hideturtle()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(50)
    turtle.begin_fill()
    turtle.fillcolor('yellow')
    turtle.circle(50)
    turtle.end_fill()
    turtle.exitonclick()


# practise4()

def practise5():
    string = input()
    nus = eval(string)
    lst = string.split(',')
    # lst.sort(reverse=True)
    print(type(nus))
    print(lst)


# practise5()

def practise6():
    new_v = [0] * 61
    old_v = [0] * 61  # 经过5分钟之后已经成熟的病毒数量 >=4的元素才有效
    total_v = [0] * 61
    N = int(input())
    new_v[0] = 1
    old_v[4] = 1
    for i in range(N):
        if i >= 5:
            old_v[i] = old_v[i - 1] + old_v[i - 4]
        if i >= 4:
            new_v[i] = new_v[i - 4] + old_v[i - 1]
        if i == 0:
            total_v[i] = 1
        total_v[i] = total_v[i - 1] + new_v[i]
    print(total_v[N - 1])

# practise6()

def homework_turtle():
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

homework_turtle()
