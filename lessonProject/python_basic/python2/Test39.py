# 查询跳远成绩
names = ("A", "B", "C", "D", "E", "F", "G")
scores = (197,234,266,251,147,321,226)
print("请输入要查询同学的姓名：")
n = input()
if n in names:
    i = names.index(n)  #找出n在names元组中的位置
    print(n,"同学的跳远成绩是",scores[i],"cm")
    #scores元组中对应位置是该同学的跳远成绩
else:
    print("没有查询到此同学")
