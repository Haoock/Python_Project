def jc(n):
    i = 1
    s = 1
    for i in range(1,n+1):
        s = s * i
    return s






#实现n的阶乘
def jc(n):
    if n == 1:
        return 1
    else:
        return n *jc(n - 1)
print(jc(5))








