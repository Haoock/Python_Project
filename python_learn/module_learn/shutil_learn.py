import shutil
# shutil是一种更高层次的文件操作工具

# 将文件内容拷贝到另一个文件中
shutil.copyfileobj(open('../../lessonProject/Data/file/file.txt', 'r'), open('../../lessonProject/Data/file/new.txt', 'w'))


