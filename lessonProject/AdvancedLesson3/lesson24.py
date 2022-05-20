# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/3/26 2:13 下午
# @Function:
from turtle import *
import turtle


def homework1():
    n = int(input())
    total_sum = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            total_sum += 1 / i
    else:
        for i in range(1, n + 1, 2):
            total_sum += 1 / i
    print("%.5f" % total_sum)


# homework1()


def homework2():
    M = int(input())
    print(M % 2)


def test():
    str1 = input()
    str2 = "DDD"
    if str1.find(str2, 0) != -1:
        print("Y")
    else:
        print("N")


# test()


# homework2()

def homework3():
    str1 = input()
    str2 = input()
    if str1.find(str2, 3) != -1:
        print("Y")
    else:
        print("N")


# homework3()


def practise1():
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


# practise1()

def practise2():
    turtle.screensize(800, 600, 'white')
    turtle.circle(100, -180)
    # turtle.pencolor('brown')
    # turtle.forward(100)
    # turtle.left(120)
    # turtle.forward(100)
    # turtle.left(120)
    # turtle.forward(100)
    # turtle.setheading(270)  # turtle.seth()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.exitonclick()


# practise2()

def practise_test():
    turtle.screensize(800, 600, 'white')
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(100, 45)
    turtle.forward(100)
    turtle.goto(0, 0)
    turtle.exitonclick()


# practise_test()


def practise3():
    turtle.pensize(2)
    for i in range(4):
        turtle.fd(150)
        turtle.left(90)
        turtle.circle(150, -45)
        turtle.goto(0, 0)
        turtle.left(45)
    turtle.exitonclick()


# practise3()

def practise4():
    turtle.pensize(2)
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150, 45)
    turtle.fd(150)
    turtle.goto(0, 0)
    turtle.left(45)
    turtle.exitonclick()


def practise5():
    turtle.pensize(2)
    for i in range(4):
        turtle.fd(150)
        turtle.left(90)
        turtle.circle(150, -45)
        turtle.goto(0, 0)
        turtle.left(45)
    turtle.exitonclick()


# practise5()

def homework():
    turtle.pensize(2)
    for i in range(4):
        turtle.fd(100)
        turtle.circle(20, 180)
        turtle.fd(100)
        turtle.right(90)
    turtle.exitonclick()

homework()
