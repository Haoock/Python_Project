# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/1/16 2:41 下午
# @Function:


# week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# # 输出星期一？星期日？
# print(week[0])
# print(week[6])
# # 输出最后一个元素的两种方法？
# print(week[-1])
# # 输出倒数第三个元素？
# print(week[-3])
# # 如何计算1到100所有数字相加之后的和？
# s = 0
# for i in range(1, 101):
#     s += i
# print(s)

#
# s1 = [range(1, 101)]
# print(s1)

# 统计所有的字符
str = input()
countEng = 0
countK = 0
countNum = 0
countOther = 0
for s in str:
    # print("%c" %s, end=" ")
    if 'a' <= s <= 'z':
        countEng += 1
    elif s == ' ':
        countK += 1
    elif '1' <= s <= '9':
        countNum += 1
    else:
        countOther += 1
print(countEng)
print(countK)
print(countNum)
print(countOther)