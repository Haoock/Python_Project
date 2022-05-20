class Dog():
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        print("Hi there, I'm a", self.species,
              ",my name is", name, ", and I'm", age, "years old.")

    def bark(self):
        print("woof-woof~ woof-woof~~ woof-woof~~~")

    def sit(self):
        print(self.name, "is now sitting!")

    def roll_over(self):
        print("A", self.species, "names", self.name, "is now rolling over!")

    # 修改属性值
    def updateAge(self, newAge):
        self.age = newAge
        """
        还可以设置age的范围，如果设置的age小于0就发出错误警告
        """

