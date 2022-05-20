# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5 8:38 上午
# @Function:
import random


# from Dog import Dog


def last_homework1():
    r = int(input('N:'))
    s = set()
    for i in range(r):
        s.add(random.randint(1, 100))
    print(s)
    s = list(s)
    s.sort()  # 排序的作用
    for x in s:
        print(x, end=" ")


# last_homework1()


def last_homework2():
    lst1 = [1, 2, 3, 5, 6, 3, 2]
    lst2 = [2, 5, 7, 9]
    st1 = set(lst1)
    st2 = set(lst2)
    if not st1.isdisjoint(st2):  # isdisjoint：如果它们没有交集返回True
        print(st1.intersection(st2))
    else:
        print("没有交集")
    print("下面的整数在lst1中，不在lst2中：", st1.difference(st2))
    print("两个列表一共有这些整数：", st1.union(st2))


# last_homework2()

def greet_users(names):  # 形式参数
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
    """修改列表中的元素"""
    names[0] = "Will"


# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)
# print(usernames)

# 通过下面的方式可以向函数传递一个usernames的副本
# greet_users(usernames[:])
# print(usernames)

def make_pizza(test, *toppings):
    """打印顾客点的所有配料"""
    print(toppings)  # *表示元组类型，一般参数


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():  # **user info是字典类型，使用的是关键字实参
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

# practise1：
# def make_album(s_name, a_name):
#     describe_album = {}
#     describe_album["singer_name"] = s_name
#     describe_album['album_name'] = a_name
#     return describe_album


# while True:
#     x = input("请输入歌手名称和专辑名称：")
#     if x == 'q':
#         break
#     lst_input = x.split(",")
#     da_name = make_album(lst_input[0], lst_input[1])
#     print(da_name)

"""
my_dog1 = Dog('pug', 'Bill', 2)
my_dog2 = Dog('jondo', 'Will', 4)

my_dog1.bark()
my_dog1.sit()
my_dog2.roll_over()
print(my_dog1.species)
print(my_dog2.age)

# 修改对象属性值的第一种方法：直接修改法
my_dog2.age = 3
print(my_dog2.age)

# 修改对象属性值的第二种方法：通过类中的方法来修改
my_dog2.updateAge(5)
print(my_dog2.age)
"""


# 定义门票类，需要自己思考一下

# usernames = ['h', 'y', 'm']
# t = usernames[:]  #
# print(t)

# 有返回值的函数
def make_album(*names):
    dic = {"singer_name": names[0], "album_name": names[1]}
    return dic


# while True:
#     x = input("请输入歌手名称和专辑名称")
#     if x == 'q':
#         break
#     lst = x.split(",")
#     res = make_album(lst[0], lst[1])
#     print(res)
