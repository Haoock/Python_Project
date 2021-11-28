import random
n = int(input('请输入题目的数量：'))
def ct():
    i = 0
    j = 0
    while i < n:
        a = random.randint(0,10)
        b = random.randint(0,10)
        print(a, "+" ,b, "=")
        c = int(input("请输入答案："))
        d = a + b
        if d == c:
            print("答题正确！")
            j +=10
        else:
            print("答题错误！")
        i += 1
    print("一共答题数量为：%d"%i)
    print("答题得分为：%d"%j)


ct()

