def ncf(x, n = 2):
    t = n
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print("%d的%d次方是%d" %(x,t,s))

ncf(5)
ncf(5,3)

