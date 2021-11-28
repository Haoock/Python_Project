# x = [10, 7, 12, 6, 3, 14]
# 第一步封装成函数：输入6个数字
def first_input():
    lst_input_temp = []
    for i in range(0, 6):
        print("请输入第%d个数字：" % (i + 1))
        x = int(input())
        lst_input_temp.append(x)
    return lst_input_temp


lst_input = first_input()
print(lst_input)
# 第二步：寻找最大的数字并将它放到最前面的元素
max_num = max(lst_input)
max_num_index = lst_input.index(max_num)
# 交换
a = max_num
lst_input[max_num_index] = lst_input[0]
lst_input[0] = max_num
print(lst_input)
# 第二步：寻找最小的数字并将它放到最后面的元素
min_num = min(lst_input) # 1
min_num_index = lst_input.index(min_num)
# 与列表中最后一个位置的元素交换
b = min_num
lst_input[min_num_index] = lst_input[len(lst_input) - 1]
lst_input[len(lst_input) - 1] = min_num
print(lst_input)




