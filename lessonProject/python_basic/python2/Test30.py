# 实现a + b并返回结果
def add(a,b):
    print("a的值是：", a)
    print("b的值是：", b)
    res = a + b   # res是一个变量，
    return res





x = 1
y = 11
# 调用add函数
# x和y都是必须参数，一个都不能缺省，参数的顺序不变
z = add(y, x)
print(z)

























'''
def identify(string):
    i = 0
    flag = False
    while i < len(string) / 2:
        if string[i] != string[len(string) - 1 - i]:
            print("这个串不是回文串")
            flag = True
            break
        i += 1
    if flag == False:
        print("这个串是回文串")
        '''


        
