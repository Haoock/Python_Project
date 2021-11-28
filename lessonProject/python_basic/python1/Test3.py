str_input = input("请输入明文：")
str_result = ""
for i in range(len(str_input)):
    str_temp = chr(ord(str_input[i]) + 3)
    str_result = str_result + str_temp
print("加密后的密文为：",str_result)

str_result2 = ""
for i in range(len(str_result)):
    str_temp = chr(ord(str_result[i]) - 3)
    str_result2 = str_result2 + str_temp
print("解密后的明文为：",str_result2)
    
