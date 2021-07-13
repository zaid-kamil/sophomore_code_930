from turtle import *

s = Screen()
s.setup(1000,700)
speed(0)
colors = ['purple','blue','pink']
pensize(3)

for i in range(10,0,-1):
    penup()
    goto(0,-20 *i)
    pendown()
    begin_fill()
    fillcolor(colors[i%3])
    begin_fill()
    circle(20 *i)
    end_fill()
hideturtle()
mainloop()