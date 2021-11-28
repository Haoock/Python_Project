biggest_num = int(input("Please enter a biggest num"))
smallest_num = int(input("Please enter a smallest num"))

for num in range(smallest_num, biggest_num + 1):
    if num > 1:
        flag = True  # flag为False说明某个数字不是素数
        for i in range(2, num):
            if num % i == 0:
                # 说明num不是一个素数
                flag = False
                break
        if flag:
            print(num)
