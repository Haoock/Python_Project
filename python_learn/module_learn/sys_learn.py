# 在 Python 中，sys 模块是一个非常常用且十分重要的模块，通过模块中的 sys.argv 就可以访问到所有的命令行参数，它的返回值是包含所有命令行参数的列表(list)。
import sys

def main():
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    print('脚本名为：', sys.argv[0])
    for i in range(1, len(sys.argv)):
        print('参数 %s 为：%s' % (i, sys.argv[i]))


if __name__ == "__main__":
    print("这是测试代码")
    main()


"""
当运行以下命令：
python sys_learn.py ouyangpeng csdn

输出：
参数个数为: 3 个参数。
参数列表: ['sys_learn.py', 'ouyangpeng', 'csdn']
脚本名为： sys_learn.py
参数 1 为：ouyangpeng
参数 2 为：csdn


python test.py ouyangpeng csdn -u username -p password

输出：
参数个数为: 7 个参数。
参数列表: ['test.py', 'ouyangpeng', 'csdn', '-u', 'username', '-p', 'password']
脚本名为： test.py
参数 1 为：ouyangpeng
参数 2 为：csdn
参数 3 为：-u
参数 4 为：username
参数 5 为：-p
参数 6 为：password

"""
print(f"Usage: {sys.argv[0]} <path-to-cmake-api-index.json> <spdx-output-dir> <spdx-namespace-prefix>")
print("fdasfds{}".format(sys.argv[0]))