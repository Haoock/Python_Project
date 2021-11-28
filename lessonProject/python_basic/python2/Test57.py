class Student:  #Student为类的名称（类名）每个单词的首字母大小
    native_place = '上海'  #直接写在类里面的变量，称为类属性

    # 下面是类的构造方法，该方法在类实例化的时候会自动调用
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def eat(self):
        print('学生在吃饭')

    def drink(self):
        print("学生在喝水")



stu1 = Student('张三',20)
print(type(stu1))


print(stu1.native_place)

stu1.eat()      # 对象名.方法名()

stu1.drink()

print(stu1.name)
print(stu1.age)
