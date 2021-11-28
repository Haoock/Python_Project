weight = float(input("请输入你的体重："))
height = float(input("请输入你的身高："))
BMI = weight / (height * height)
print(BMI)
if BMI < 18.5:
    print("你偏瘦了！")
elif BMI >= 18.5 and BMI < 25:
    print("你是健康的！")
elif BMI >= 25 and BMI < 30:
    print("你偏胖啦！")
elif BMI >= 30 and BMI < 35:
    print("你过于肥胖！")
elif BMI >=35:
    print("你是极度肥胖！")
