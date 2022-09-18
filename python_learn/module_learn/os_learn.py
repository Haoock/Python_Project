import datetime
import os
import os.path as path

path_name = '~/file.txt'

# path.expanduser
full_path = path.expanduser(path_name)
print(full_path)
# /Users/{username}/file.txt
# C:\Users\Haock/file.txt
'''
在windows路径中这个路径添加出来会变成反斜杠，这里要注意
'''

##########################################################################################
# path.join
path_name2 = "//"

# 下面的两个输出是一样的
print(path.join(path_name2, "Data", "file.txt"))
print(path.join(path_name2, "Data/", "file.txt"))
# windows: //Data\file.txt
# mac：    /Users/{username}/PycharmProjects/lessonProject/Data/file.txt

# 输出会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
print(path.join(path_name2, "Data", "/file.txt"))
# /file.txt

# 最后一个文件为空
print(path.join(path_name2, "Data", "Documents", ""))
# /Users/{username}/PycharmProjects/lessonProject/Data/Documents/

##########################################################################################
path_str = "../Data/file/file2.txt"
nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
# os.rename(path_str, '../Data/file/file1.txt' + ".bak-%s" % nowTime)

#######
# 找到当前文件所处的目录
print(os.path.dirname(__file__))

##########################################################################################
# 分割最后一个文件名和前面的路径名
path_str = '/home/User/Desktop/file.txt'
head_tail = os.path.split(path_str)  # /home/User/Desktop/
print(head_tail)  # file.txt
norm_path = os.path.normpath(path_str)
print(norm_path)

##########################################################################################
path_str = '../Data/file/file.txt'
if path.exists(path_str):
    print("存在该文件！")
else:
    print("不存在该文件！")


##########################################################################################
# os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
# 它会返回三个参数：curDir，dirs，files
# 默认情况下是采用自顶向下的方式进行扫描
for curDir, dirs, files in os.walk(r"E:\py  thon"):
    print("====================")
    print("现在的目录：" + curDir)
    print("该目录下包含的子目录：" + str(dirs))
    print("该目录下包含的文件：" + str(files))
print("结束！！！")
# 如果要自底向上地扫描子目录和文件，可以添加上topdown=False参数：
for curDir, dirs, files in os.walk(r"E:\python", topdown=False):
    print("====================")
    print("现在的目录：" + curDir)
    print("该目录下包含的子目录：" + str(dirs))
    print("该目录下包含的文件：" + str(files))

# 使用os.walk输出某个目录下的所有文件
for curDir, dirs, files in os.walk(r"E:\python"):
    for file in files:
        print(os.path.join(curDir, file))

# 也可以利用os.walk输出test文件夹下指定后缀名（比如.txt）文件：
for curDir, dirs, files in os.walk("test"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(curDir, file))

# 同样地，我们也可以利用os.walk输出test文件夹下所有的子目录（子文件夹）：
for curDir, dirs, files in os.walk("test"):
    for dir in dirs:
        print(dir)

relative_path = os.path.relpath(r"E:\python\python1", r"E:\python")
print(relative_path)

