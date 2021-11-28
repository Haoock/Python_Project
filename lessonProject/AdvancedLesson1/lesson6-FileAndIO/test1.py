# my_file = open('ppap.txt')
# for line in my_file:
#     # print(line)
#     # 如果要去掉空白行，需要使用rstrip函数
#     print(line.rstrip())
#

with open('ppap.txt') as file_object:
    contents = file_object.read()
    print(contents)

