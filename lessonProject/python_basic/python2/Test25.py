def jc(n):
    i = 1
    s = 1
    for i in range(1, n + 1):
        s = s * i
        i+=1
    return s

a = int(input("请输入一个数："))
print("这个数的阶乘是：", jc(a))
