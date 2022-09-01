# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/4
# @Function:

import random  # import 模块名
# random.randint()

# import random as r # import 模块名 as
# r.randint()

# import random as r, turtle as t  #  import 模块名1 as 别名1，模块名2 as 别名2










# from random import randint # from 模块名 import 成员名

# randint()










# from random import randint as rt   # from 模块名 import 成员名 as 别名


# rt()




# from random import randint, choice  #   支持一次导入多个模块

# from random import *

# choice()

# import Dog
# dog = Dog()



import Demo

# print(__name__)
# print(Demo.__name__)


# 异常处理

# test1：

# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print()
# print(5 / 0)

# test2
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = 0
    try:
        answer = int(first_number) / int(second_number)
    except Exception:
        print("不允许除以零的操作")
    print(answer)
"""

# 下面是正确的代码,加入了异常处理

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# test3

# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print("文件不存在！")
# else:
#     print("....")


# test4
"""
from get_name import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
"""

# test5

# import unittest
# from get_name import get_formatted_name
#
#
# # 这是一个与测试相关的类，最好要包含Test字样
# # 并且这个类必须继承unittest.TestCase类，Python才能知道如何运行你编写的测试。
# class NameTestCase(unittest.TestCase):
#     # 用于测试get_name.py
#
#     # 所有以test_打头的方法都将自动运行
#     def test_first_lastname(self):
#         formatted_name = get_formatted_name('Jack', 'joplin')
#         # unittest类最有用的功能之一：一个断言方法
#         self.assertEqual(formatted_name, 'Jackjoplin')
#
#
# # 让Python运行这个文件中的测试。
# unittest.main

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0



class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

# man = Man

# print('stRF'.lower())
# print('stRF'.upper())
# print('sfdsa'.title())

# from Person import Person
# from Man import Man
# baby = Man("蓝宝", 18)
# baby.judge_earn_money()
# baby.work()
# baby.display_money()

