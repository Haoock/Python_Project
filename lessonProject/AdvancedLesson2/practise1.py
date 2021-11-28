"""
蓝桥杯练习：给定一个单词及文章，

"""


def finds(aa, bb):
    n = 0
    while len(bb) != 0:  # 当bb为空的时候停止
        if bb.find(aa) != -1:
            n = n + 1
            bb = bb[bb.find(aa) + len(aa) - 1:len(bb)]
        else:
            break
    return n


a = ' ' + input().upper() + ' '
b = ' ' + input().upper() + ' '
if b.find(a) == -1:
    print(-1)
else:
    print(finds(a, b), b.find(a))
