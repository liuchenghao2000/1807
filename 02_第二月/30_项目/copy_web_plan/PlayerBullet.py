#<code class="language-plain">
import pygame  
from Bullet import *  
  
class PlayerBullet(Bullet):  
    enemies=[]  
    info=0  
    def draw(self,enemies,screen):  
        self.enemies=enemies  
        self.frame=screen  
        self.y-=self.speed  
        if self.y<0:  
            self.bullet.remove(self)  
        self.frame.blit(self.img,(self.x,self.y))  
          
        for ene in self.enemies:
            if self.x>ene.x and self.x<ene.x+57 and self.y>ene.y and self.y<ene.y+43:  
                self.enemies.remove(ene)
                self.bullet.remove(self)