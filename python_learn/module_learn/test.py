# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/1/15 12:51 下午
# @Function:
# import sys_learn
from collections import defaultdict
from configparser_learn import import_test
import_test()

# str1 = "asdf"
# str2 = str1
# print(id(str2))
# print(id(str1))
#
# num1 = 12
# num2 = num1
# print(num1)
# print(id(num2))
# print(id(num1))  # 这是一个引用赋值，两个id都相同
#
# num3 = 20
# num4 = num3
# num3 = 21
# print(num4)
# print(id(num3))
# print(id(num4))  # 这是一个拷贝赋值，两个id都不同
#
# lst1 = [1, 2, 3, 4]
# lst2 = lst1
# lst3 = lst1[:]  # 这其实就是浅拷贝
# lst1[2] = 99
# print(lst2)
# print(id(lst1))
# print(id(lst2))
# print(id(lst3))
#
#
# def tst(a):
#     a[3] = 90
#     print(a)
#
#
# b = [1,1,2,3]
# tst(b)
# print(b)
# sys_learn.main()

# node_dict = defaultdict(int)
# # node_dict["asdf"]["hahaha"] = 0
# # print(node_dict["asdf"]["hahaha"])
# node_name = ""
# for i in range(10):
#     node_dict["asdf"] += i if node_name != '' else 0
# print(node_dict["asdf"])

