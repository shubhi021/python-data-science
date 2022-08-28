import pgzrun
from random import randint


HIEGHT =500
WIDTH = 500

p= Actor('ironman',(10,10))
speed=3

def draw():
    screen.clear() #to clear screen so that no after dragging effect is left on screen
    screen.fill('blue')
    
    p.draw()

def update():
    player_control()
  

def player_control():
    if keyboard.RIGHT and not p.right > WIDTH: #for moving right on screen
        p.x +=speed
    elif keyboard.LEFT and not p.left < 0:
        p.x +=-speed
    elif keyboard.UP and not p.top < 0:
        p.y +=-speed
    elif keyboard.DOWN and not p.bottom > HIEGHT:
        p.y +=speed
    else:
        p.angle = 0            


pgzrun.go()#outside the function    