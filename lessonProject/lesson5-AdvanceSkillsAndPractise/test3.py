import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width = 100, height = 100)
canvas.pack()

canvas.create_rectangle(20, 20, 60, 60)
