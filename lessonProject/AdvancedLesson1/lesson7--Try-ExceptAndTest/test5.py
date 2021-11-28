import unittest
from get_name import get_formatted_name

# 这是一个与测试相关的类，最好要包含Test字样
# 并且这个类必须继承unittest.TestCase类，Python才能知道如何运行你编写的测试。
class NameTestCase(unittest.TestCase):
    '''用于测试get_name.py'''
    # 所有以test_打头的方法都将自动运行
    def test_first_lastname(self):
        formatted_name = get_formatted_name('Jack', 'middle','joplin')
        # unittest类最有用的功能之一：一个断言方法
        self.assertEqual(formatted_name, 'Jack Joplin')
# 让Python运行这个文件中的测试。
unittest.main()

