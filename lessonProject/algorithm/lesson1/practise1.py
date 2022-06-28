# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2022/2/20 9:15 上午
# @Function:


def mysqrt(x):
    left, right = 1, x
    while left < right:
        mid = (right - left) / 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1


if __name__ == "__main__":
    x = int(input())
    print(mysqrt(x))


