def count_words(file):
    count = 0
    # 根据文件中的空格统计
    with open(file) as file_object:
        lines = file_object.readlines()
    for line in lines:
        words = line.split()
        count += len(words)
    return count

file_name = "ppap.txt"
count_num = count_words(file_name)
print(count_num)
    
    
