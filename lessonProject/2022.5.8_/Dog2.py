# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/15 10:42 上午
# @Function:
import random  # Python内置的类
import math

class Dog():
    def __init__(self, s, n, a):  # 初始化函数，初始化静态属性，创建实例的时候一定会调用的函数
        self.specie = s
        self.name = n
        self.age = a
        print("初始化方法调用")

    def bark(self):  # 狗叫的方法，动态属性
        print("woof~woof~woof~woof~")

    def sit(self):  # 狗坐下，动态属性
        self.bark()
        print(self.name, "sit down")

    def roll_over(self):  # 狗翻跟头,动态属性
        print(self.specie, self.name, "rolling over")


dog = Dog("pug", "will", 3)  # dog 是一个实例
dog.sit()
print(dog.specie)

random.randint(10, 18)
random.choice([1, 24, 56])
