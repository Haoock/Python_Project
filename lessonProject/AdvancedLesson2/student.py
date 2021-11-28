class Student:
    def __init__(self, id_num, name, age):
        self.id = id_num
        self.name = name
        self.__age = age

    def print_student(self):
        print("学生的学号为：", self.id)
        print("学生的姓名为：", self.name)
        print("学生的年龄为：", self.__age)


class ClassPresident(Student):
    def __init__(self, id_num, name, age, course_name, course_score):
        super(ClassPresident, self).__init__(id_num, name, age)
        self.courseName = course_name
        self.courseScore = course_score

    def print_student(self):
        super().print_student()
        print("该位学生是", self.courseName, "的课代表")
        print("该位学生的成绩是", self.courseScore)


student1 = Student("123", "hao", 15)
class_president1 = ClassPresident("123", "hao", 15, "English", 99)
class_president1.print_president()





