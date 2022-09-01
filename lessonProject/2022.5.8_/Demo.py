# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/6/4
# @Function:
name = "Python Learning！"
add = "I love Python"


def say():
    print("人生苦短，我学Python！")


class Language:
    def __init__(self, name, add):
        self.name = name
        self.add = add

    def say(self):
        print(self.name, self.add)


if __name__ == "__main__":
    print("开始输出")
    say()
    clangs = Language(name, add)
    clangs.say()
    print(__name__)
