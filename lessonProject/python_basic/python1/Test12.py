lc = int(input("输入路程："))
sj = int(input("输入等待时间："))
if lc >= 10:
    fy = 6 + (10 - 3) * 1.8 + (lc - 10)*1.8 *1.5 #行程大于10公里的收费
else:
    if lc > 3:
        fy = 6 + (lc - 3) * 1.8
    else:
        fy = 6
fy = fy + (sj/3) * 1
print("车费是：%10.2f" % fy)
