import math
def ms(n):
    if n <= 1:
        print(n,"不是素数")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(n,"不是素数")
            break
        else:
            print(n,"是素数")

m = int(input("请输入一个数："))
ms(m)
