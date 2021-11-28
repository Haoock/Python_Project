score = [98,87,78,93,75,92,90]
a = max(score)
b = min(score)
print("去掉一个最高分：",a)
score.remove(a) #删除第一次出现的最高分
print("去掉一个最低分：",b)
score.remove(b) #删除第一次出现的最低分
average = sum(score) / len(score)
print("最终得分是：",average)
