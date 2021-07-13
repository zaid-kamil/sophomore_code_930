from turtle import *

color('red')
begin_fill()
while True:
    forward(200)
    left(150)
    print(abs(pos()))
    if abs(pos()) < 1:  # turtle reaches its original position
        break           # stop or break the loop
end_fill()
mainloop()