print("100-999之间的水仙花数有：")
for i in range(100, 1000):
    j = int(i / 1 % 10)  # 个位 使用int的原因是强转故意让其损失精度,Python中使用此方法获取时必须强转因为Python中默认保留小数
    k = int(i / 10 % 10)  # 十位
    m = int(i / 100 % 10)  # 百位
    if i == (j ** 3 + k ** 3 + m ** 3):
        print(i)
