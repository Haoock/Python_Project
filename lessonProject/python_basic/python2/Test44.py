#找到第二大的数有两种做法

# 1：第一种是使用max函数，然后再将这个数删去，然后再使用max函数
list1 = [1,2,3,4,5]
x = max(list1)
list1.remove(x)
print(max(list1))



# 2:第二种是使用sort函数，然后直接取出第一个和第二个值

list2 = [1,2,3,4,5]
list2.sort(reverse = True)
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
print(list2)
