# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
#
#
# while True:
#     name = input("Please enter a pizza name!")
#     make_pizza(name)
#     if name == 'q':
#         break
from random import *
from math import *

# from turtle import *
# def tree(plist,l,a,f):
#     if l>2:
#         nextlist=[]
#         for p in plist:
#             p.forward(l)
#             q=p.clone()
#             p.left(a)
#             q.right(a)
#             nextlist.append(p)
#             nextlist.append(q)
#         tree(nextlist,l*f,a,f)
# def main():
#     p=Turtle()
#     p.color("green")
#     p.speed(10)
#     p.pensize(1)
#     p.left(90)
#     p.hideturtle()#隐藏箭头
#     p.penup()#抬笔
#     p.goto(-100,-100)
#     p.pendown()#落笔
#     tree([p],90,60,0.65)
#     done()
# main()

# 1,23,45,6
string = input()
lst = string.split(",")
print(lst)
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# print(lst)

lst = list(eval(string))
total_num = 0
for x in lst:
    total_num += x
print("%.2f" % (total_num / len(lst)))
length = len(lst)
# 1, 4, 5, 6
if length % 2 == 0:
    mid = int(length / 2)
    mid_num = (lst[mid] + lst[mid - 1]) / 2
else:
    mid_num = lst[int(length / 2)]
print(mid_num)
lst.sort()
count = 0
number = -1 # 假设的众数
# for x in lst:
#     if x != number:
#         if



