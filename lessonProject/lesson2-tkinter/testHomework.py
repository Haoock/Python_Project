
# 第一个for循环控制每一行的元素
for i in range(9,0, -1):
    # 第二个for循环是控制每一行中列的元素
    for j in range(1, i+1, 1):
        # 每一行的输出元素不换行
        print("%d * %d = %2d "%(i, j, i*j), end = '')
    # 每一行输出之后换行
    print()

    

# 第一个for循环控制每一行的元素
for i in range(1,10):
    # 第二个for循环是控制每一行中列的元素
    for j in range(1, i+1, 1):
        # 每一行的输出元素不换行
        print("%d * %d = %2d "%(i, j, i*j), end = '')
    # 每一行输出之后换行
    print()

    
