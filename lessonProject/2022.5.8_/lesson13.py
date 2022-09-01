# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/28
# @Function:
import random


class Number:
    def __init__(self, n1=8, n2=4):
        self.__n1 = n1
        self.__n2 = n2

    def addition(self):
        m1 = self.__n1 + self.__n2
        print("n1和n2的和为：%s" % m1)

    def subtration(self):
        m2 = self.__n1 - self.__n2
        print("n1和n2的差：%s" % m2)

    def multiplication(self):
        m3 = self.__n1 * self.__n2
        print("n1和n2的乘积为：%s" % m3)

    def division(self):
        m4 = self.__n1 / self.__n2
        print("n1和n2除为：%s" % m4)


# 第一种做法，直接在类的函数中输出结果
# calculator = Number(8, 19)
# calculator.addition()
# calculator.subtration()
# calculator.multiplication()
# calculator.division()


# 第二种做法，类的函数返回结果并输出
class RandomGen:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    def generate(self):
        res = []
        for i in range(self.count):
            res.append(random.randint(self.start, self.end))
        return res

    def generate_coor(self):
        nums = self.generate()
        for i in range(0, len(nums) - 1, 2):
            print("(%d,%d)" % (nums[i], nums[i + 1]))


# r = RandomGen(20, 100, 20)  # 实例化一个随机生成整数类
# print(r.generate())  # 调用r对象调用generate这个函数生成5个随机数。
# r.generate_coor()


from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        # print("初始化")

    def roll_die(self):
        i = 0
        if i <= 10:
            for n in range(11):
                print(randint(1, self.sides), end=" ")
                i += 1
            print("\n")


# die = Die()
# die.roll_die()
# die = Die(10)
# die.roll_die()
# die = Die(20)
# die.roll_die()


class Animal:
    def eat(self):
        print("It is eating")

    def drink(self):
        print("It is drinking!")

    def run(self):
        print("It is running!")

    def sleep(self):
        print("It is sleeping!")


class Dog(Animal):
    def bark(self):
        print("It it barking!")


class Cat(Animal):
    def scratch(self):
        print("It it scratching!")


class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        print("说人话")
        super.bark()


# keji = Dog()  # 实例化一个狗的对象
# keji.eat()      # keji调用eat这个方法
# keji.run()
# keji.drink()
# keji.sleep()
# keji.bark()
#
# maomi = Cat


# 1
class Number:
    n1 = 0
    n2 = 0

    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2

    def addition(self):
        return self.n1 + self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def subtration(self):
        return self.n1 - self.n2

    def division(self):
        return self.n1 / self.n2


# number = Number(n1=5, n2=5)
# print("和为", number.addition())
# print("商为", number.division())
# print("积为", number.multiplication())
# print("余为", number.subtration())
# computer = number


# 2
class RandomGen():
    def _init_(self, happy):
        self.happy = happy

    def happy(self):
        a = random.randint(20, 100)
        return a


# randomgen = RandomGen()
# m = []
# for happy in range(1, 21):
#     m.append(happy)
# print(m)
# 3
import random


class Die():
    def __init__(self, sides=6):
        self.sides = sides  # 属性名称为sides,面数

    def roll_die(self):
        a = random.randint(1, self.sides)
        return a

    def play(self):
        results = []
        for roll in range(10):
            result = self.roll_die()
            results.append(result)
        print(results)


# die = Die()  # 创建6面的骰子
# die.play()   # 掷骰子
#
# die2 = Die(10)  # 创建10面的骰子
# die2.play()
#
# die3 = Die(20)  # 创建20面的骰子
# die3.play()

class rect():
    def __init__(self, a, b):
        self.a = a  # 长
        self.b = b  # 宽

    def calculate_square(self):
        square = self.a * self.b
        print("面积是：%.2f" % square)


class square(rect):
    def __init__(self, a, b, c):
        super().__init__(a, b)  # 通过a和b初始化父类
        self.c = c  # square的实例属性

    def print_square(self):
        print("正方形的边长是：%d" % (self.a))


x = square(5 , 5, 10)
x.print_square()
x.calculate_square()
