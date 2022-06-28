# def MyFun(nums):
#     # 创建新列表
#     mydict = {}
#     for i in nums:
#         if i not in mydict:
#             mydict[i] = 1
#         else:
#             mydict[i] += 1
#     for k, v in mydict.items():
#         if v >= 2:
#             return k
#
#
# nums = [2, 1, 4, 5, 6, 4]
# print(MyFun(nums))
f = open('pi_digits', mode='b')
print(f.readline())

