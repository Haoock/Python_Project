nums = [1, 2, 5, 8, 4]
target = int(input("Please enter a target number:"))
# 第一层循环是为了找第一个元素
# 加一个flag标志，用来判断是否已经有两个元素满足了要求
flag = False
for i in range(len(nums)):
    if flag:
        break
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
            flag = True
            break


