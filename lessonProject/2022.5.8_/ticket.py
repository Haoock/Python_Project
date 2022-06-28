# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/15 11:21 上午
# @Function:

class Ticket():
    def __init__(self, w=False, c=False):
        self.weekend = w
        self.child = c  # 默认是成人
        self.price = 100

    def calc_Rrice(self, num):  # num指的是人数
        if self.weekend:  # 是周末
            self.price *= 1.2
        if self.child:   # 是儿童
            self.price *= 0.5
        total_price = self.price * num
        return total_price


ticket = Ticket(True, True)  # 买的周末的儿童票
print(ticket.calc_Rrice(1))
ticket2 = Ticket(True)  # 买的是周末的成人票
print(ticket2.calc_Rrice(2))

