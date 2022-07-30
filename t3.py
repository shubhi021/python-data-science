from turtle import *

side = 6
size = 100
pencolor('red')
pensize(3)
speed('fastest')

for i in range (side): 
    pencolor('red')
    forward(size) 
    for i in range (side): 
        pencolor('green')
        forward (size//2)
        left(360/side)
    left(360/side)
     
mainloop()