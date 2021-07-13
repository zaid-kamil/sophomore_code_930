from turtle import *
from random import randint

speed(0)

for i in range(100):
    up()
    goto(randint(-200,200),randint(-200,200))
    down()
    fd(50)
    left(90)
    fd(50)
    left(90)
    fd(50)
    left(90)
    fd(50)
    left(90)

