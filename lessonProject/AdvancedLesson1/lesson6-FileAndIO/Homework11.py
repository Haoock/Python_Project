with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)  # string类型

with open('learning_python.txt') as file_object:
    for i in range(3):
        contents = file_object.readline()
        print(contents)  # string类型

lst = []
with open('learning_python.txt') as file_object:
    for i in range(3):
        contents = file_object.readline()
        lst.append(contents)
    print(lst)