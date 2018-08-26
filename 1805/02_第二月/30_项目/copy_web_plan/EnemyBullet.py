import pygame
from Bullet import *
 
class EnemyBullet(Bullet):
 
    def draw(self):
        self.y+=self.speed
        if self.y>600:
            self.bullet.remove(self)
        self.frame.blit(self.img,(self.x,self.y))