# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/2/20 2:50 下午
# @Function:

x = int(input())
# for i in range(1, x):
#     if i % 2 == 0:
#         print(0)

result = 0
for i in range(1, (x + 1) // 2):
    result = result + 2
    print(result)


