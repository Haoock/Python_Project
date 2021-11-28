#方法一：
lst=[1,3,5,3,4,4,2,9,6,7]
set_lst=set(lst)
#set会生成一个元素无序且不重复的可迭代对象，也就是我们常说的去重
if len(set_lst)==len(lst):
    print('列表里的元素互不重复！')
else:
    print('列表里有重复的元素！')



#方法二：

lst=[1,3,5,8,9,9,0,0,3,3]
new_list=[]
 
for i in lst:
    if i not in new_list:
        new_list.append(i)
        #这样能确保新的列表里包含原列表里所有种类的元素，且元素互不重复
 
if len(new_list)==len(lst):
    print('原列表里的元素互不重复！')
else:
    print('原列表里有重复的元素！')
