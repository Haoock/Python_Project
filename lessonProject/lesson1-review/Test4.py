list1 = (91,92,92,94,95)
max_count = 0
max_num = -1
for i in list1:
    count = list1.count(i)
    if count > max_count:
        max_count = count
        max_num = i
print(max_num)    
