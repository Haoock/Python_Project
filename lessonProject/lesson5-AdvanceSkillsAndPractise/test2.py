class Student():
    # 构造函数
    # 对当前对象的实例的初始化
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    #   isinstance函数判断一个对象是否是一个已知的类型，类似type
    def get_name(self):
        if isinstance(self.name, str):
            return self.name

    def get_age(self):
        if isinstance(self.age, int):
            return self.age

    def get_course(self):
        a = max(self.score)
        if isinstance(a, int):
            return a


zm = Student('zhangming', 20, [69, 88, 100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
