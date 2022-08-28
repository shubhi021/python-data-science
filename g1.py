import pgzrun
HIEGHT = 400
WIDTH = 600

p=Actor('ironman',pos=(100,100))

def draw():
    screen.clear()
    screen.draw.text("Welcome to pgzero",(10,10),color='red',fontsize=50)
    screen.draw.text('created by shubhi',(10,360),color='white')
    p.draw()

#outside function
pgzrun.go()

