# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/14  上午
# @Function:
import turtle


def last_homework1_temp1():
    start = "A"
    start_idx = ord(start)
    for x in range(start_idx, start_idx + 26):
        print(chr(x), end=" ")


# last_homework1_temp1()


def last_homework1_temp2():
    start = 'A'
    start_idx = ord(start)
    for x in range(start_idx + 3, start_idx + 26 + 3):
        idx = (x - start_idx) % 26  # 控制在26以内
        print(chr(idx + start_idx), end=" ")


# last_homework1_temp2()


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


# last_homework3()
# 5 4 3 2 1
# 12345
# 1234
# 123
# 12
# 1
def printDigit(n):
    print(n % 10, end="")
    if n > 10:
        printDigit(int(n / 10))


def algorithm_practise1():
    n = int(input())
    printDigit(n)


algorithm_practise1()

def ten_to_two(n):
    res = []
    if n == 0:
        return [0]
    while n != 0:
        res.insert(0, n % 2)
        n = int(n / 2)
    return res


def algorithm_practise2():
    n = int(input())
    res = []
    for x in range(n + 1):
        r = ten_to_two(x)
        res.append(r.count(1))
    print(res)


# algorithm_practise2()

def binary_search(nums, target):
    # nums是已经排好序的列表数组 1, 2, 3, 4, 5, 6
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + right
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


# print(binary_search([1, 2, 3, 4, 5, 6], 7))
# lst = [1, 2, 5, 8, 10, 15]
# lst.insert(3,6)
# print(lst)


# a = input("").split(" ")  # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# for n in a:
#     x = ord(n)
#     x1 = x + 3
#     if x1 > ord("Z"):
#         print(chr(x1 - ord("Z") + ord("A") - 1))
#     else:
#         print(chr(x1))

numbers = list(eval(input()))
target = int(input())
res = []
flag = False
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            if numbers[i] + numbers[j] == target:
                res.append(i)
                res.append(j)
                flag = True
                break
    if flag:
        break
print(res)


# 10的二进制数：
# 靖哲：10110
# 雨辰：1010 （正确）

# print(bin(20)[2:])
# print(type(bin(10)))
# print(bin(20))


# n = int(input())
# res = []
# for i in range(n + 1):
#     b = bin(i)[2:]   # str类型
#     b_lst = list(b) # ['1', '0']   [1, 0, 1]
#     temp = b_lst.count("1")
#     res.append(temp)
#
# print(res)


# nums = list(eval(input()))
# target = int(input())
# # nums里面是否存在target
# temp_num = nums.count(target)
# if temp_num == 0:  # 说明这个数组中不存在target
#     # 寻找正确的target所在的位置
#     for i in range(len(nums)):
#         if nums[i] > target:
#             print(i)
#             break
# else:
#     print(nums.index(target))


s = input()



