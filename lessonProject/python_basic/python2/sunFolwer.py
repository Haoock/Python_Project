import turtle
import time
# 设置画布的大小
turtle.screensize(800,600,)
# 设置窗体的大小
turtle.setup(800,600)
print(turtle.pos())
turtle.pensize(1)
turtle.pencolor('red')
turtle.speed(5)
turtle.fillcolor('yellow')

turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
time.sleep(1)
turtle.done()
