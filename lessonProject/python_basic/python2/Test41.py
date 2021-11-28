def f(n):
    # 1.先写递归结束条件
    if n <= 2:
        return 1;
    # 2.接着写等价关系式
    return f(n-1) + f(n - 2);


print(f(8))
