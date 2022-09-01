# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/8/6
# @Function:
import turtle


def last_homework1():
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


# last_homework1()

def last_homework2():
    turtle.screensize(800, 600)
    turtle.setup(900, 700)
    turtle.pencolor('yellow')
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.right(60)  # 为了让第一个三角形和后面的三角形for循环里面处理一致
    colors = ["pink", "green", "blue", "purple"]
    for i in range(4):
        turtle.pencolor(colors[i])
        turtle.left(150)
        for i in range(2):
            turtle.forward(70)
            turtle.right(180 - 60)
        turtle.forward(70) # 画第三条边的时候不需要转向
    turtle.exitonclick()


# last_homework2()

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
    max_appearance_num_temp = -1  # 众数出现的最多次数
    max_appearance_num = -1
    max_appearance_temp = -1  # 众数
    max_appearance = -1
    sum_num = 0
    for i in range(num_len):
        sum_num += num_tup[i]
        if max_appearance_temp == num_tup[i]:
            max_appearance_num_temp += 1
        else:
            max_appearance_num_temp = 1
            max_appearance_temp = num_tup[i]
        if max_appearance_num_temp > max_appearance_num:
            max_appearance_num = max_appearance_num_temp
            max_appearance = max_appearance_temp
    print("%.2f" % (sum_num / num_len))
    print("%.2f" % mid_num)
    print(max_appearance)


# algorithm_practise1()

def algorithm_practise2():
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


# algorithm_practise2()

def algorithm_practise3():
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
        turtle.goto(0,0)
    turtle.exitonclick()

# algorithm_practise3()

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
        if checkPos(row, j):  # 检查当前行和j列的位置是否合法（是否有皇后存在）
            Queen[row][j] = 1  # 将这个位置放置一个皇后
            eightQueen(row + 1)  # 递归进入下一行
            Queen[row][j] = 0  # 回溯回来将皇后取消放置


# 输出放置所有八皇后的棋盘。"★"表示放置了皇后
def print_Queen():
    for i in range(8):
        for j in range(8):
            if Queen[i][j] == 1:
                print('☆ ' * j + '★ ' + '☆ ' * (7 - j))
    print("*" * 20)


eightQueen(0)
print(total_num)

# a = [1, 3, 5, 8]
# res = []
# for i in range(4):
#     for j in range(4):
#         for x in range(4):
#             c = str(a[i]) + str(a[j]) + str(a[x])
#             res.append(int(c))
# for i in range(len(res)):
#     print(res[i])
#
# import turtle as t
# import random
# t.speed(1)
# t.right(30)
# a = ['yellow', 'pink', 'purple', 'blue', 'green']
# for i in range(4):
#     b = random.randint(0, 4)
#     t.pencolor(a[b])
#     t.circle(35, steps=3)
#     t.right(90)
# t.penup()
# t.left(90)
# t.forward(100)
# t.right(90)
# t.pendown()
# c = random.randint(0, 4)
# t.pencolor(a[c])
# t.right(180)
# t.circle(100)
# t.exitonclick()

# a = list(eval(input()))
# sum_total = 0
# for x in a:
#     sum_total += x
# print("%.2f" % (sum_total / len(a)))
#
# mid_num = -1
# if len(a) % 2 != 0:
#     mid_num = a[len(a) // 2]
# else:
#     mid_num = (a[len(a) // 2] + a[len(a) // 2 + 1]) / 2
# print("%.2f" % mid_num)
#
# most_num = -1  # 众数
# most_num_appearence = -1 # 众数出现的次数
# for x in a:
#     temp = a.count(x) # 对x进行数数的次数
#     if temp >= most_num_appearence:
#         most_num = x
# print(most_num)

# for i, j in zip(range(8), range(5, 13)):
#     print(i ,j)


