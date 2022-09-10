import pgzrun
from random import randint

HIEGHT = 800
WIDTH =1000

ps = 3 #player speed
es = 3 # emny speed

game_over = False #switch
game_started = False #switch

center = (WIDTH//2,HIEGHT//2)

bg = Actor('bg', center=(80,100))
p = Actor('ironman',pos=(100,100))
e = Actor('zombie',pos=(700,100))

def show_screen_1():
    #screen.fill('#ffff00') #
    bg.draw()
    screen.draw.text('Our Game',center=center,fontsize=100, color='white')
    screen.draw.text('Press Space to start',center=(center[0],center[1]+100),fontsize=50,color='white')

def show_game_screen():
    bg.draw()
    p.draw()
    e.draw()

def draw():
    screen.clear()
    if not game_started:    
        show_screen_1()
    elif game_startrd()
        show_game_screen()    

def update():
    global game_started
    if keyboard.SPACE and not game_started:
        game_started = True
        bg.image = 'bg'
    if game_started and not game_over:
        player_control()
        enemy_control()

def player_control():
    if keyboard.RIGHT and not p.right > WIDTH: #for moving right on screen
        p.x += ps
        p.angle = -10
    elif keyboard.LEFT and not p.left < 0:
        p.x += -ps
        p.angle = 10
    elif keyboard.UP and not p.top < 0:
        p.y += -ps
    elif keyboard.DOWN and not p.bottom > HIEGHT:
        p.y += ps
    else:
        p.angle = 0            
            
def enemy_control():
    global game_over
    if p.x > e.x:
        e.x += es
    if p.x < e.x:
        e.x += -es
    if p.y > e.y:
        e.y += es
    if p.y < e.y:
        e.y += -es 
    if p.colliderect(e):
        game_over = True

pgzrun.go()                