count = 0
while True:
    name = input("请输入姓名：")
    sents = name + "，欢迎您来到此程序！"
    print(sents)
    count += 1
    record = "时间：2021年11月28日，第" + str(count) + "位访客,姓名是：" + name + "\n"
    with open("guest_book.txt", "a") as fileobject:
        fileobject.write(record)
        print("记录写入成功！")
    x = input("输入q退出此程序")
    if x == 'q':
        break