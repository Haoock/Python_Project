# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/2/27 1:06 下午
# @Function:

# for i in range(1, 5):
#     print(int(i + (i-1)) * '*')

# for i in range(1, 8):
#     if i <= 4:
#         print(int(i + (i - 1)) * '*')
#     else:

# for i in range(1, 5):
#     for j in range(int(i + (i - 1))):
#         print('*', end='')
#     print()

# for i in range(1, 5):
#     for j in range(i * 2):
#         print("*", end="")
#     print()

# for i in range(9, 2, -2):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(1, 101):
#     a = i % 7
#     if a == 0:
#         print(i)


a = "This is an apple"
x = a.split(' ')
print(x)
for a in x:
    print(a, end="~")


# b = x.index('an')
# x[b] = 'a'
# x[b + 1] = 'pear'
# print(x)


str = "This is an apple"
index = 0
length = len(str)
for i in range(len(str)):
    # print(str[i])
    if str[i] == ' ':
        index += 1
    # if 'a' <= str[i] <= 'z' and 'A' <= str[i] <= 'Z':
    #     print(str[i])
    #     index += 1
print(length - index)

