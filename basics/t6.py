from turtle import *

value = 400

while value > 0:
    forward (value)
    lt(90)
    value -= 20
    write(value)
mainloop()