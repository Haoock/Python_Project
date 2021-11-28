i = 5
while i > 0:
    j = 1
    str = ''
    while j <= i:
        str = str + '* '
        j = j + 1
    print(str)
    i = i - 1

print("")


i = 1
while i <= 5:
    j = 1
    str = ''
    while j <= 5:
        str = str + '* '
        j = j + 1
    print(str)
    i = i + 1
print("")



























for i in range(5,0,-1):
    str = ''
    for j in range(0,i):
        str += '* '
    print(str)


