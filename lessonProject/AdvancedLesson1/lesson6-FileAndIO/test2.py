'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
'''

# 下面去除换行符,文件中的空格
# read和readlines到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。
file_name = "pi_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()


pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)



