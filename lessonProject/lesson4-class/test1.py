class Dog():
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        print("Hi there, I'm a",self.species,
            ",my name is", name, ", and I'm", age, "years old.")
    
    def bark(self):
        print("woof-woof~ woof-woof~~ woof-woof~~~")

    def sit(self):
        print(self.name,"is now sitting!")

    def roll_over(self):
        print("A", self.species, "names", self.name, "is now rolling over!")

    # 修改属性值
    def updateAge(self, newAge):
        self.age = newAge
        """
        还可以设置age的范围，如果设置的age小于0就发出错误警告
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




