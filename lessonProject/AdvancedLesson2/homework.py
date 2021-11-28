class Fruit():
    def __init__(self, in_price=0, out_price=0, num=0, init_price=1000):
        self.__in_price = in_price
        self.out_price = out_price
        self.__num = num
        self.init_price = init_price

    # 进货
    def in_product(self, in_price, in_num):
        self.in_price = in_price
        self.num += in_num
        self.init_price -= in_price * in_num

    # 销售
    def out_product(self, out_price, out_num):
        self.out_price = out_price
        self.num -= out_num
        self.init_price += out_price * out_num

    # 输出当前的本金
    def print_condition(self):
        print(self.init_price)
        print(self.num)


# 主程序
fruit1 = Fruit()
fruit1.in_product(18, 50)
fruit1.out_product(22, 30)
fruit1.init_price = 0
fruit1.num = 0