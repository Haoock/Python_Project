card1 = ("天蝎座","射手座","摩羯座","水瓶座","双鱼座")
card2 = ("巨蟹座","狮子座","处女座","天秤座","双鱼座")
card3 = ("金牛座","处女座","摩羯座","水瓶座","双子座","天秤座")
card4 = ("白羊座","狮子座","射手座","双子座","水瓶座","天秤座")
cardlist = (card1,card2,card3,card4)

con = ("白羊座","金牛座","双子座","巨蟹座","狮子座","处女座",
       "天秤座","天蝎座","射手座","摩羯座","水瓶座","双鱼座")

def showcard(card):
    for c in card:
        print(c,end=" ")
    print()

key=""
for c in cardlist:
    showcard(c)
    print("你的星座在这里吗？(y/n)")
    flag = input()
    if flag == "y" or flag == "Y":   #如果星座在卡片上就输入y
        key+="1"
    else:
        key+="0"
index = int(key,2)
print("你的星座是：",con[index - 1])
         
