import tkinter

# 首先定义好要显示出来的文本
explanation = """At present,only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily
中文字体！"""


# 创建一个tkinter根对象
root = tkinter.Tk()
# 设置root的这个对话框的小标题
root.title("label learning")
# 创建一个Label对象，并以root为根对象，后面的参数分别有不同的意义
w = tkinter.Label(root,fg = 'green',bg = 'blue',text = explanation,padx = 200,pady = 100,relief = 'sunken')
# label对象的组织形式是pack（包装）
w.pack()
# 进入主循环（让tkinter运行起来）
root.mainloop()

'''
root = Tk()
root.title("lable learning")
#w = Label(root,fg = 'red',bg = 'green',text = explanation,padx = 100,pady = 100)
#w = Label(root,fg = 'red',bg = 'green',text = explanation,padx = 100,pady = 100,font=('楷体',20),wraplength=100,underline=0)
#w = Label(root,fg = 'red',bg = 'green',text = explanation,padx = 100,pady = 100,font=('楷体',20),justify = CENTER)


w.pack()
root.mainloop()
'''
