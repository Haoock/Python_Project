# 导入tkinter的包
import tkinter
# 创建出tkinter的对象
root = tkinter.Tk()
# 创建出两个列表组件--->(父对象是root对象)
listb1 = tkinter.Listbox(root)
listb2 = tkinter.Listbox(root)
# 同时创建出两个数据列表
li = ['C', 'Python', 'php', 'html', 'Sql', 'java']
movie = ['css', 'Jquery', 'Bootstrap']
#将第一个组件封装数据
for item in li:
    listb1.insert(0,item)
# 将第二个组件封装数据
for item in movie:
    listb2.insert(0,item)

# 管理控件的区域组织形式是（包装）
listb1.pack()
listb2.pack()

# 进入消息循环
root.mainloop()
