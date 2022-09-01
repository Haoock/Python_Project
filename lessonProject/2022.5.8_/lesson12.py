# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/15 11:54 上午
# @Function:
import random

class Student():
    num = " "
    def __init__(self, name, age, grades):
        self.name = name
        self.__age = age
        self.__grades = grades

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.__age)

    def get_course(self):
        return max(self.__grades)

    def set_age(self, temp_age):
        if 0 < temp_age < 150:
            self.__age = temp_age
        else:
            print("错误！你输入的年龄不符合规范")


stu1 = Student("张三", 20, [69,83,71])
stu2 = Student("李四", 22, [90,80,70])
stu1.set_age(-10)
# print(stu1._Student__age)
# stu1.age = -10

# age = stu1.get_age()

# stu1.get_course()  # 手动调用了get——course这个方法
# # bbq.go()
# Student.num = "32"
# print(stu1.num)
# print(stu2.num)

# print(stu._Student__age)
# print(stu.get_course())


# 首先尝试编写make_car函数
def make_car(make, model, **others):
    car = {"make": make, "model":model}
    for key, value in others.items():
        car[key] = value
    print(car)


class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, **others):
        """初始化描述汽车的属性"""
        car = {"make": make, "model": model}
        for key, value in others.items():
            car[key] = value
        self.car_info = car
        if self.car_info["tow_package"]:
            self.__miles = 30  # 私有的属性
        else:
            self.__miles = 50
        print("汽车品牌是:", self.car_info["make"], "汽车的型号是：", self.car_info["model"], "汽车的颜色是：", self.car_info["color"], "汽车是否装配配件：", self.car_info["tow_package"])

    def __print_miles(self): # 私有的方法，只能类的内部去访问
        print("该汽车的里程是", self.__miles, "万公里")

#
# car = Car("本田", "XR-V7", color='blue', tow_package=True)
# car.print_miles()


# 自己定义的随机整数生成类
# class RandomGen:
#     def __init__(self, start, end, count):
#         self.start = start
#         self.end = end
#         self.count = count
#
#     def generate(self):
#         res = []
#         for i in range(self.count):
#             res.append(random.randint(self.start, self.end))
#         return res
#
# r = RandomGen(5, 20, 100) # 实例化一个随机生成整数类
# print(r.generate())  # 调用r对象调用generate这个函数生成5个随机数。
#
#

# lst = [12 ,13, 15, 20]
# lst.append(90)
# lst.pop(len(lst) - 1)


class stack():
    def __init__(self, stack_lst):
        self.stack_lst = stack_lst
        print("初始化成功")

    # 将某个元素入栈
    def push(self, num):
        self.stack_lst.append(num)
        print("入栈成功")

    def pop(self):
        self.stack_lst.pop(len(self.stack_lst) - 1)
        print("出栈成功！")

    def visit_top(self):
        print("栈顶元素是：%d" % self.stack_lst[len(self.stack_lst) - 1])  # 使用一般的方法
        print("栈顶元素是：%d" % self.stack_lst[-1])  # 使用切片的方法

    def is_empty(self): # 判断是否是空栈
        if len(self.stack_lst) == 0:
            print("True")
        else:
            print("False")

    def get_length(self):
        return len(self.stack_lst)


# di = 123
# f = 123.4
# s = "124"
# print("栈顶元素是 %8.3f" % di)
# print("栈顶元素是", f)


# 格式化输出
# %d ：表示专门输出int（整数）
# %3d: 输出的数字占3位
# %s ：专门输出str（字符串类型）
# %f ：专门输出float类型（）
# %.3f：保留三位小数输出


















# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return int(self.age)
#     def get_course(self):
#         a=list(self.grade.values())
#         return a
# student_01=Student('zhangming',20,{'语文':69,'数学':88,'英语':100})
# print(student_01.get_name())
# print(student_01.get_age())
# print(student_01.get_course())
# #2
# def make_car(manufacturer,model,**car_info):
#     profile = {}
#     profile['汽车的品牌是:'] = manufacturer
#     profile['汽车的型号是:'] = model
#     for key, value in car_info.items():
#         profile[key] = value
#     return profile
#
# tow_package='汽车是否装配件'
# car=make_car('本田', 'XR-V7', color='blue', tow_package=True)
# print(car,'该汽车的里程数是30公里')

class RandomGen():
    def __init__(self, num, end, start=5):
        self.num = num
        self.start = start
        self.end = end

    def generate(self):
        res = []
        # 生成随机数
        for i in range(self.num):
            t = random.randint(self.start, self.end)
            res.append(t)
        return res

# r1 = RandomGen(5, 100)
# y = r1.generate()
# print(y)
# r2 = RandomGen(10, 20)
# y = r2.generate()
# print(y)


