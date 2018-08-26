import pygame
 
class Bullet(object):
 
    def __init__(self,x,y,screen,bullet):
        self.img=pygame.image.load("bullet1.png")
        self.x=x
        self.y=y
        self.frame=screen
        self.speed=4
        self.bullet=bullet