import tkinter as tk


# 定义点击按钮时候触发的函数
def say_hello():
    print("You pressed hello button, Hello World!")


def quit():
    print("You pressed quit button!")


root = tk.Tk()
root.geometry("200x100")

button_hello = tk.Button(root, text="Hello", fg='green', command=say_hello)
button_hello.grid(row=0, column=0)
button_quit = tk.Button(root, text="quit", fg = 'red', command=quit)
button_quit.grid(row=0, column=1)


root.mainloop()



