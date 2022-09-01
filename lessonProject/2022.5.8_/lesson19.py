# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/7/9 15:35
# @Function:
import turtle


# 冒泡排序算法v2以及统计元素所交换的次数
def homework(arr):
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


# arr = [12, 11, 13, 5, 6]
# res = homework(arr)
# print(res)


def practise1():
    n = int(input())
    total_sum = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            total_sum += 1 / i
    else:
        for i in range(1, n + 1, 2):
            total_sum += 1 / i
    print("%.5f" % total_sum)


# practise1()

# str.find(str, beg=0, end=len(string))
def practise2():
    str1 = input()
    str2 = input()
    if str1.find(str2, 0) != -1:
        print("Y")
    else:
        print("N")


# practise3()

def t_practise1():
    # 正方形或者长方形
    turtle.screensize(800, 600, 'white')
    turtle.pencolor('brown')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.exitonclick()


# t_practise1()

# 三角形加正方形
def t_practise2():
    turtle.screensize(800, 600, 'white')
    # turtle.circle(100, -180)
    turtle.pencolor('brown')
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.setheading(270)  # turtle.seth()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.exitonclick()


# t_practise2()

def practise_test():
    turtle.screensize(800, 600, 'white')
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(100, 45)
    turtle.forward(100)
    turtle.goto(0, 0)
    turtle.exitonclick()


# practise_test()
# 小风车叶片
def t_practise3():
    turtle.pensize(2)
    for i in range(4):
        turtle.fd(150)
        turtle.left(90)
        turtle.circle(150, -45)
        turtle.goto(0, 0)
        turtle.left(45)
    turtle.exitonclick()


# t_practise3()

# 绘制一个正方形内切一个圆
def t_practise4():
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


# t_practise4()

# 使用递归算法逆序输出各位数字
def print_digit(n):
    print(n % 10, end="")
    if n > 10:
        print_digit(int(n / 10))


# print_digit(12345)

# for i in range(1, 101):
#     for j in range(1, 101):
#         for k in range(1, 101):
#             if i + j + k == 100 and i * 5 + j * 3 + k / 3 == 100:
#                 print("公鸡有{}，母鸡有{}，小鸡有{}",i, j, k)

# 1
# a = int(input(''))
# if a > 0 and a < 10:
#     print('个位数')
# if a < 100 and a > 9:
#     print('十位数')
# if a < 1000 and a > 99:
#     print('百位数')
# if a < 10000 and a > 999:
#     print('千位数')
# if a < 100000 and a > 9999:
#     print('万位数')
# a = str(a)
# a = a[::-1]
# print(a)
# a=int(input(''))
# b=str(a)
# for i in range(1,a+1):
#     i=str(i)
#     if i==i[::-1]:
#         print('是回文')
#         print(i)
