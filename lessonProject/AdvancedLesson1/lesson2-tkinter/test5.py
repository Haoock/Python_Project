import tkinter as tk

#首先定义tkinter的根对象
root = tk.Tk()
#更改窗口的标题和大小
root.title("Button Learning")
root.geometry('1000x600')
#在tkinter根对象的基础上创建两个button对象
label1 = tk.Label(root,fg = 'red', bg = 'green', text = "First")
label2 = tk.Label(root,fg = 'red', bg = 'green', text = "second")
label3 = tk.Label(root,fg = 'red', bg = 'green', text = "third")
# 将两个button控件以grid布局的方式展现出来
label1.grid(row = 0, column = 0)
#label2.grid(row = 3, column = 0)
label3.grid(row = 0, column = 3)
# 和后面的效果是一样的
label2.grid(row = 1, column = 0)


#进入主循环（让tkinter运行起来）
root.mainloop()
