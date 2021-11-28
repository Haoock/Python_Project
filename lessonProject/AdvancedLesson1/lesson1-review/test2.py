# a是公里数
a = int(input("请输入公里数："))
# b是时间
b = int(input("请输入时间："))

if a <= 3: # 3公里以内
    cost = 6
elif a < 10: # 10公里以内
    cost = 6 + (a-3) * 1.8
else:   # 10公里以上
    cost = 6 + (a-10) * 2.7 + (a-7) * 1.8

cost = cost + a / 3

# cost是最后花费的费用
print(cost)
