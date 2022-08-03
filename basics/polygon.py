from turtle import *

speed('slowest')
pencolor('black')
bgcolor('blue')

side = 5
size = 100
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()