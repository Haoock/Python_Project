filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
print('写入文件成功')

# 可以尝试读取该文件的内容
#with open(filename) as file_object:
#    print(file_object.read())

    
