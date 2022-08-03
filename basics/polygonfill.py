from turtle import *

speed('slowest')
pencolor('black')
bgcolor('white')
pensize(10)

side = 5
size = 100
fillcolor('green')
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()
mainloop()