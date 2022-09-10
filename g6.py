import pgzrun
from random import randint
HEIGHT=800
WIDTH=1000
ps=3 # player speed
es=3 #speed of enemy
game_over=False #Flag #switch
game_started=False #switch
center=(WIDTH//2,HEIGHT//2)#points to center coordinates of screen
bg=Actor('bg',center=(0,0))
p=Actor('ironman',pos=(100,100))
e=Actor('zombie',pos=(700,100))
def show_screen_1():#will show this funvtion if the game is not started
    bg.draw()
    screen.draw.text('Our Game',center=center,fontsize=100,color='black')
    screen.draw.text('press SPace to start',center=(center[0],center[1]+100),fontsize=50,color='white')
def show_game_screen():
    bg.draw()
    p.draw()
    e.draw()
    pass
def show_game_over():
    pass
def draw():
    screen.clear()
    if not game_started:
        show_screen_1()
    else:
        show_game_screen()    
def update():
    global game_started
    if keyboard.SPACE and not game_started:
        game_started=True 
        bg.image='bg'
    if game_started and not game_over:
        player_control()
        enemy_control()
def player_control():
    if keyboard.RIGHT and not p.right>WIDTH:
        p.x+=ps
        p.angle=-10
    elif keyboard.LEFT and not p.left<0:
        p.x+=-ps
        p.angle=10
    elif keyboard.DOWN and not p.bottom >HEIGHT:
        p.y+=ps
    elif keyboard.UP and not p.top<0:
        p.y+=-ps
    else:
        p.angle=0                
def enemy_control():
    if p.x>e.x:
        e.x+=es
    if p.x<e.x:
        e.x+=-es    
    if p.y>e.y:
        e.y+=es
    if p.y<e.y:
        e.y+=-es    
    if p.colliderect(e):
        game_over=True      
pgzrun.go()