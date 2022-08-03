from turtle import *

pencolor('yellow')
pensize(3)
speed('slowest')

for i in range (5):
    forward(100)
    for i in range(6):
        pencolor('red')
        forward (100)
        pencolor('yellow')

        left(360/6)
    left(360/5)

mainloop()