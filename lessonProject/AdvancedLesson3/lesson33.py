# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/4
# @Function:

def lastHomework_way1():
    s = input()
    res = len(s.split()[-1])
    print(res)


# lastHomework_way1()

def lastHomework_way2():
    s = input()
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1
    if end < 0:
        return
    start = end
    while start >= 0 and s[start] != ' ':
        start -= 1
    print(end - start)


# lastHomework_way2()

# f = int(float(input("请输入一个数字")) * 100)
# money = [1, 2, 5, 10, 20, 50, 100]
# money_lastIndex = len(money) - 1
# count_num = 0
# for i in range(money_lastIndex, 0, -1):
#     num = int(f / money[i])
#     if num == 0:
#         continue
#     # print(num)
#     f %= money[i]
#     print("剩余金钱数量是：", f)
#     count_num += num
# print(count_num)

class my_stack:
    def __init__(self, lst):
        self.lst = lst

    # 进栈的函数
    def in_stack(self, num):
        self.lst.append(num)
        print("入栈成功")

    def out_stack(self):
        self.lst.pop()
        print("出栈成功")

lst = []
stack1 = my_stack(lst)
stack1.in_stack(9) # 进栈的操作
stack1.out_stack()




