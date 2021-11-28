# 首先要求用户输入两个数字

num1 = int(input("请输入第一个数字a的值："))
num2 = int(input("请输入第二个数字b的值："))
print("交换之前：a = ",num1)
print("交换之前：b = ",num2)
num3 = num1
num1 = num2
num2 = num3
print("交换之后：a = ",num1)
print("交换之后：b = ",num2)