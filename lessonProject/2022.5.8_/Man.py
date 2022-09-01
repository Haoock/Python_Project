# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/5 10:31
# @Function:
from Person import Person


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.earn_money = 50

    def judge_earn_money(self):
        if self.age >= 18:
            self.earn_money = 100

    def work(self):
        self.money += self.earn_money

    def display_money(self):
        print(self.name + "今年" + str(self.age) + "岁，拥有资产" + str(self.money) + "元")
