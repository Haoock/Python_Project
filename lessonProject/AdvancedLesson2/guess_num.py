class Game():
    def __init__(self, number=100):
        self.__number = number

    def judge_num(self, a):
        if a > self.__number:
            print("You entered a big number!")
        elif a < self.__number:
            print("You entered a small number!")


num = int(input("Please enter a number"))
# game1的实例化
game1 = Game()
game1.judge_num(num)