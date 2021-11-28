#求斐波那契数列第n项的值
def f(n):
    if n <= 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(6))
