sum = 0
ml = 1
for i in range(1,65,1): #循环64次
    sum = sum + ml
    ml = ml * 2
    print(i,ml,sum)     #打印次数，每次麦粒数量，此次循环麦粒的累加总数
print(sum)
