Monday = ["咒语", "魔法棋","变形术"]
Tuesday = ["生物", "读心术", "飞行课"]
Wednesday = ["魔法史", "天文", "如尼文"]
Thursday = ["占卜", "草药", "天文"]
Friday = ["变形术", "黑魔法", "魔药"]
schedule = [Monday,Tuesday,Wednesday,Thursday,Friday]
print("周一上午：",Monday[2])    #输出周一下午的一节课
print("周二上午：", Tuesday[0:2])    #输出周二上午的两节课

#对于下午的课程，可以认为是这一天的最后一节课
#所以程序可以采用反向索引的方法进行查询
#周一下午的课程就可以用Monday[-1]表示
#周二上午的两节课则可以用Tuesday[-3:-1]表示
