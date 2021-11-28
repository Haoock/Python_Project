b = input("请输入一个二进制数：")
s = 0.0
for i in range(len(b)):
    s += int(b[len(b) - 1 - i]) * pow(2,i)
print("转换成十进制的数是：%d" %s)

print("第二种二进制转十进制的方法为：%d" %int(b,2))





c = int(input("请输入一个正整数"))
temp = c
str_result = ""
while c != 0:
    str_result += str(c % 2)
    c = c // 2
print(str_result[::-1])

print("第二种二进制转十进制的方法为:" ,bin(temp))



