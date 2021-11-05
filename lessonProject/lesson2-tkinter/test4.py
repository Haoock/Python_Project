from tkinter import *

# 下面的可以将三个标签放在同一行中
root = Tk()
root.title('label learning')
#geometry函数是专门用于设置tkinter窗口的大小
root.geometry("600x600")

# 设置三个Label，都以root为根对象。
lab1 = Label(root, text="Red Sun", bg="red", fg="white")
lab2 = Label(root, text="Green Grass", bg="green", fg="black")
lab3 = Label(root, text="Blue Sky", bg="blue", fg="white")
# 将三个label分别以left的方式，并且排列充满整个root窗口，在竖直方向填充
#lab1.pack(side = "left",padx = 50,pady = 60,ipadx = 30,ipady = 20)
lab1.pack(side = "left",expand = True,fill = Y)
lab2.pack(side = "left",expand = True,fill = Y)
lab3.pack(side = "left",expand = True,fill = Y)

# 让程序运行起来
mainloop()



