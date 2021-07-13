from turtle import *
bgcolor('black')
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
speed('fastest')
for i in range(260):
    pencolor(colors[i % 6])
    pensize(i/100+1)
    forward(i)
    left(59)
mainloop()
