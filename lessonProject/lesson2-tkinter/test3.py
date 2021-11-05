import tkinter as tk
# 首先定义根对象
root = tk.Tk()


# 以root作为根对象定义Label对象
# label1使用anchor参数
label1 = tk.Label(root, anchor = "w", width = 100, height = 100,text = "Hello World",font = ('黑体',20))
# label2使用justify参数
label2 = tk.Label(root, justify = "right",width = 100, height = 100,text = "Hello World\nhahah",font = ('黑体',20))
# label3使用image参数，要使用image参数必须要导入图片
label_image = tk.PhotoImage(file = 'test_pic.png')
label3 = tk.Label(root, anchor = "center", image = label_image)
# label4使用wraplength参数
label4 = tk.Label(root, wraplength = 2, text = "HelloWorld",anchor = "center", width = 100, height = 100)


# label以怎样的方式布局到根对象中（包装）
label4.pack()
# 进入主循环（启动tkinter）
root.mainloop()
