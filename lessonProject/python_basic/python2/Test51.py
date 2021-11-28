foodsdict = {"苹果":5,"梨子":2,"桃子":5,"菠萝":7,"香蕉":3}


ft = 3.1415926
print("%0.3f"%ft, end = "")


print("目前存储的食物情况：")
for f,n in foodsdict.items():
    print(f,"有",n,"个")

while True:
    print("新增的食物是什么？（输入q终止）",end = "")
    name = input()
    if name == 'q' or name == 'Q':
        break
    print("数量有多少个呢？",end="")
    num = input()
    if name in foodsdict.keys():
        foodsdict[name] += int(num)
    else:
        foodsdict[name] = num

print("补充库存之后，目前存储的食物情况：")
for f,n in foodsdict.items():
    print(f,"有",n,"个")
