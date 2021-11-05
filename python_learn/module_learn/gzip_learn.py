import gzip

# gzip的使用与文件的读写是类似的

# 首先使用gzip压缩某个文件
# rb:以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# gzip只能以二进制的形式进行读写文件
with open('../Data/file/file.txt', 'rb') as f_in:
    with open("../Data/file/file.gz", 'wb') as f_out:
        f_out.write(f_in.read())

##########################################################################################
# 使用gzip解压缩某个文件 目前这样的写法出了问题
with gzip.open('../../lessonProject/Data/file/file.gz', 'rb') as f:
    file_content = f.read()
