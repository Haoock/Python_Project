import random
secret = random.randint(1,10)
# print(secret)
print("====猜数字游戏====")
guess = 0
while guess != secret:
    temp = input("请输入数字：")
    guess = int(temp)
    if guess == secret:
        print("恭喜，您猜对了！")
        print("游戏结束！再见")
    if guess > secret:
        print("您输入的数字太大了！")
    elif guess < secret:
        print("您输入的数字太小了！")
