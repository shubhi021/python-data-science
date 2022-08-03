from turtle import *

penup() # for the pointer to not make any line just move
goto(-100,100)
goto(100,100)
pendown()
goto(100,-100)
write('  I am here')#space so that it doesnot over write
goto(-100,-100)
write('I am here', font=('airial',30,'normal'),align ='center')#for font changes
mainloop()