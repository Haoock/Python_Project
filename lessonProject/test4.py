num = int(input("Please enter a number"))
# x是num的个位，也存储最后的结果
x = num % 10
num //= 10
# 每次while循环用来取num的每一位
while num != 0:
    y = num % 10
    num //= 10
    x = x * 10 + y
print(x)
