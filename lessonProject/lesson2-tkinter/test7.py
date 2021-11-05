import tkinter as tk

def show_text():
    print(entry1.get())

root = tk.Tk()
root.geometry("200x100")

label1 = tk.Label(root, text = "First Name")
label1.grid(row = 0,column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry1.insert(1, "hahaha")
entry1.insert(3, "eeeee")


show_button = tk.Button(root, text = "show",command = show_text)
show_button.grid(row = 1)


root.mainloop()
