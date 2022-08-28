import pgzrun
from random import randint

HIEGHT =600
WIDTH = 500

music.play('bgm')

p= Actor('ironman',(100,100))
c= Actor('cookie')
c.x = randint(64, WIDTH-64)
c.y = randint(64, HIEGHT-64)

score=0
speed=3

def draw():
    #screen.clear() #to clear screen so that no after dragging effect is left on screen
    screen.fill('black')
    p.draw()
    c.draw()
    screen.draw.text(f'score:{score}',(WIDTH-80,10))
    

def update():
    player_control()
    update_score()

def update_score():
     global score
     if p.colliderect(c):  
        score += 1
        c.pos = (randint(64,WIDTH-64),randint(64,HIEGHT-64))
        sounds.eating2.play()

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