import pygame  
from pygame.locals import *  
from sys import exit  
import time
from Enemy import *
from Player import *
 
class Main(object):
    screen=""
    enemies=[]
    
    if __name__ == '__main__':
        screen = pygame.display.set_mode((400, 600), 0, 32)
        background = pygame.image.load("background.png")
          
    def __init__(self):
        print()
 
        
    player=Player(screen)
    
    mouse_x, mouse_y = 0, 0
    keyDown=True 
    info=0
    
    while True:
        for event in pygame.event.get():  
            if event.type == QUIT:  
                exit()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    if keyDown:
                        keyDown=False
            if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                player.keyhandle("mousedown",mouse_x,mouse_y,'')
        if info%10==0:
            player.keyhandle("fire",0,0,enemies)
        info+=1
        screen.blit(background, (0,0)) 
        numX=random.randint(1,370)
        
        if numX %55==0:
            enemies.append(Enemy(numX,0,screen))
        for temp in enemies:
            temp.draw()
            temp.move()
            
        player.draw() 
        pygame.display.update() 
        time.sleep(0.01)

