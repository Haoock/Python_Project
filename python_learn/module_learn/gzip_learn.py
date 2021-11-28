import gzip
import shutil
# gzip的使用与文件的读写是类似的

# 首先使用gzip压缩某个文件
# rb:以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# gzip只能以二进制的形式进行读写文件
with open('../Data/file/file.txt', 'rb') as f_in:
    with gzip.open("../Data/file/file.txt.gz", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

##########################################################################################
# 使用gzip解压缩某个文件
with open('../Data/file/file2.txt', 'wb') as out_f, gzip.GzipFile('../Data/file/file.txt.gz') as zip_f:
    out_f.write(zip_f.read())
