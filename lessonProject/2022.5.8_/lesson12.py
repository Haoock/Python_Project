# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/5/15 11:54 上午
# @Function:

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, color, tow_package):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.color = color
        self.tow_package = tow_package
        if self.tow_package:
            self.miles = 30
        else:
            self.miles = 50
        print("汽车品牌是:", self.make, "汽车的型号是：", self.model, "汽车的颜色是：", self.color, "汽车是否装配配件：", self.tow_package)

    def print_miles(self):
        print("该汽车的里程是", self.miles, "万公里")


car = Car("本田", "XR-V7", color='blue', tow_package=True)
car.print_miles()
