import pygame  
from PlayerBullet import *
class Player(object):
    enemies=[]
    def __init__(self,screen):
        self.image=pygame.image.load("hero1.png")
        self.x=200
        self.y=500
        self.speed=5
        self.planeName='player'
        self.frame=screen
        self.playerBullet=[]
    def draw(self):
        self.frame.blit(self.image,(self.x-51,self.y-55))
        for temp in self.playerBullet:
            temp.draw(self.enemies,self.frame)
        
    def keyhandle(self,keyValue,x,y,enemies):
        self.enemies=enemies
        if keyValue=="mousedown":
            self.x=x
            self.y=y
        elif keyValue=="fire":
            self.playerBullet.append(PlayerBullet(self.x,self.y-55,self.frame,self.playerBullet))