num = [32, 44, 55, 66]
citys = ['重庆', '上海', '北京', '深圳']
with open("test.txt", 'a') as file:
    print("成功")
    for i in range(len(citys)):
        str = "{}    {}".format(citys[i], num[i])
        file.write(str)
        file.write('\r\n')

print("ok")

