class Cat():
    def __init__(self, species, name, age, eye_color):
        self.species = species
        self.name = name
        self.age = age
        self.eye_color = eye_color
        print("Hello i am a", self.species,"cat. My name is",
              self.name, ",and i am", self.age, "years old with",
              self.eye_color,"eyes")
    def jump(self):
        print(self.name,"is jumping now!")

    def bark(self):
        print("miao miao miao!")

    def sleep(self):
        print(self.name, "like sleep so much")

# 波斯猫
cat_persian = Cat('persian', 'will', 2, 'blue')
cat_persian.jump()
cat_persian.bark()
cat_persian.sleep()

