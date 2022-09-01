# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/21  下午
# @Function:

def last_homework1():
    arr = list(eval(input()))
    k = int(input())
    arr.sort()
    res = []
    for i in range(k):
        res.append(arr[i])
    print(res)


# last_homework1()
# "abcba"

def last_homework2():
    arr = list(eval(input()))
    length = len(arr)
    for i in range(0, length):
        if arr[i] != i:
            print(i)
            break
        else:
            print()


# last_homework2()

def last_homework3():
    arr = list(eval(input()))
    target = int(input())
    print(arr.count(target))


# last_homework3()

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


# 将字符串中除了是英文字符之外的所有数字全都删去
# 然后再来判断是否是回文数
# def Algorithm_practise1():

# hlabcdefgijkmnopqrstuvwxyz
# worldabcefghijkmnpqstuvxyz
# abcdefghijklmnopqrstuvwxyz
def Algorithm_practise2():
    words = input()
    words = words.split(",")
    order = input()
    dic = {}
    index = 0
    for x in order:
        dic[x] = index
        index += 1
    flag = True
    for i in range(len(words) - 1):
        word_now = words[i]
        word_next = words[i + 1]
        min_len = min(len(word_now), len(word_next))
        for j in range(min_len):
            if dic[word_now[j]] < dic[word_next[j]]:  # 说明根据了字典序进行了排序
                flag = True
                break
            elif dic[word_now[j]] > dic[word_next[j]]:  # 说明没有根据字典序进行排序
                flag = False
                break
        # 需要排除特殊情况，如果当前单词和后面的单词前半部分都是一样的，那么flag依旧为false
        if len(word_now) > len(word_next):
            flag = False
        if not flag:  # 如果一次检查完成之后发现不是字典序那么直接跳出循环。
            break

    if flag:
        print("true")
    else:
        print("false")


# Algorithm_practise2()

def Algorithm_practise4():
    x = input()
    lst = x.split(" ")
    lst.reverse()
    print(lst)
    lst2 = []
    for x in lst:
        if x != '':
            lst2.append(x)
    # 将lst2以题目中的标准输出格式输出结果


# Algorithm_practise4()
# nums = list(eval(input()))   # 都是数字 int
# print(nums)
# target = int(input()) # 整数类型
# print(nums.count(target))

# def reverse_str(s):
#     b = ""
#     for x in s:
#         if 'a' <= x <= 'z':
#             b = b + x
#     return b
#
# s = input("s = ")
# s = s.lower()
# b = reverse_str(s)
# c = b
# b = b[::-1]  # 翻转字符串
# if c == b:
#     print("true")
# else:
#     print("false")


# a = input()
# a = a.lstrip()  # 原地函数左边（left）
# a = a.rstrip()  # 去除字符串右边（right）的空格

lst = ["hello", "world!"]
lst.reverse()  # reverse是一个原地函数
# print(lst)

# print(a)

a = input()
b = a.split(" ")
b.reverse()
c = ""
for x in b:
    c = c + x + " "
c = c.rsplit()
print(c)


# "abcdefgi...o"
# apple   orange
# orange  apple

# banana die
# bana   banana
# word   world

# word,world,row
# abcdefghijklmnopqrstuvwxyz
lst = input().split(",")
order = input()
c = list(order)
flag = False
for i in range(len(lst) - 1):
    now_word = lst[i]
    next_word = lst[i + 1]
    len_min = min(len(now_word), len(next_word)) # 取两个单词中最小的长度
    print(now_word,end=" ")
    print(next_word, end=" ")
    print(len_min)
    for j in range(len_min):
        now_index = c.index(now_word[j])
        next_index = c.index(next_word[j])
        if now_index > next_index:
            flag = True
            break
    if flag:
        break
if flag:
    print("false")
else:
    print("true")
