roboticsclub = ["王一凡","邓中正","谢宇翔","王启瑞","张永泰","史可兮"]
n = len(roboticsclub)
print("原社团有",n,"名学生：",roboticsclub)
for i in range(1,5):
    newname = input("请输入第"+str(i)+"名学生姓名：")
    roboticsclub.append(newname)
n = len(roboticsclub)
print("现在机器人社团有",n,"名学生：",roboticsclub)
