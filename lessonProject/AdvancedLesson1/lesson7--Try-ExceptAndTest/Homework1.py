try:
	with open("dogs.txt") as object1:
		lines = object1.readlines()
except FileNotFoundError:
	print("错误！文件不存在！")
else:
	print(lines)