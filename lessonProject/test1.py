import tkinter as tk


# 定义点击按钮时候触发的函数
def say_hello():
    print("You pressed hello button, Hello World!")


def quit():
    print("You pressed quit button!")


# 主窗口，并设置大小为200*100像素
root = tk.Tk()
root.geometry("200x100")

# 定义两个按钮，一个名称为Hello，一个名称为quit，分别将say_hello
button_hello = tk.Button(root, text="Hello", fg='green', command=say_hello)
button_hello.grid(row=0, column=0)
button_quit = tk.Button(root, text="quit", fg='red', command=quit)
button_quit.grid(row=0, column=1)

root.mainloop()
