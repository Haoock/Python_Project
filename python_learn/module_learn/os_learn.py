import datetime
import os
import os.path as path

path_name = '~/file.txt'

# path.expanduser
full_path = path.expanduser(path_name)
print(full_path)
# /Users/{username}/file.txt
'''
在windows路径中这个路径添加出来会变成反斜杠，这里要注意
'''

##########################################################################################
# path.join
path_name2 = "//"

# 下面的两个输出是一样的
print(path.join(path_name2, "Data", "file.txt"))
print(path.join(path_name2, "Data/", "file.txt"))
# /Users/{username}/PycharmProjects/lessonProject/Data/file.txt

# 输出会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
print(path.join(path_name2, "Data", "/file.txt"))
# /file.txt

# 最后一个文件为空
print(path.join(path_name2, "Data", "Documents", ""))
# /Users/{username}/PycharmProjects/lessonProject/Data/Documents/

##########################################################################################
path = "../Data/file/file2.txt"
nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
os.rename(path, '../Data/file/file1.txt' + ".bak-%s" % nowTime)

#######
# 找到当前文件所处的目录
print(os.path.dirname(__file__))