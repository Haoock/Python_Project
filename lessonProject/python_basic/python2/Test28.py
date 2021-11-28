def ss(n):
    for i in range(2, n):
        if n % i == 0:
            print(n, "不是素数")
            break
        if n == i+1:
            print(n, "是素数")

s = int(input("请输入一个数值："))
ss(s)




#上面的方法明显存在效率低下的问题
#第二种思路，我们可以进行因式分解，
#一个数一定是大于等于sqrt(n)
#另一个一定是小于等于sqrt(n)

