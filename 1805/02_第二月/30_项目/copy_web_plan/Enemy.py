import pygame
import random
from EnemyBullet import *
 
class Enemy(object):
    enemyBullet=[]
    def __init__(self,x,y,screen):
        self.img=pygame.image.load("enemy1.png")
        self.x=x
        self.y=y
        self.frame=screen
        self.enemyBullet=[]
        enemyBullet=self.enemyBullet
        self.speed=2
    def draw(self):
        self.frame.blit(self.img,(self.x,self.y))
    def move(self):
        self.y+=self.speed
                
        num=random.randint(1,100)
        if num in [1,70]:
            self.enemyBullet.append(EnemyBullet(self.x+28,self.y+43,self.frame,self.enemyBullet))
        for temp in self.enemyBullet:
            temp.draw()
