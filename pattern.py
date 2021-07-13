from turtle import *

bgcolor("black")
color("red")
speed('slow')

for i in range(1,200,10):
    print(i+5)
    fd(i+5)
    left(90)

color("blue")
for i in range(200,1,-10):
    print(i+5)
    fd(i+5)
    left(90)

mainloop()