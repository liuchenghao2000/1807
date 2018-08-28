import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
FIRE_BULLENT = pygame.USEREVENT + 1
#keys_pressed = pygame.key.get_pressed()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,imagename,speed=1):
        super().__init__()
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y+=self.speed


class EnemySprite(GameSprite):
    def __init__(self):
        self.imagename = './images/enemy0.png'
        super().__init__(self.imagename)
        self.speed = random.randint(1,5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.height:
            self.kill()

class BackGroundSprite(GameSprite):
    def __init__(self,is_alt=False):
        self.imagename = "./images/background.png"
        super().__init__(self.imagename)
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.top >=  SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Hero(GameSprite):
    def __init__(self):
        self.imagename = './images/hero1.png'
        super().__init__(self.imagename,0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 60 
        self.bullent_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        self.rect.y +=self.speed1
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom


    def fire(self):
        bullent = Bullent()
        bullent.rect.centerx = self.rect.centerx
        bullent.rect.y = self.rect.top-20
        self.bullent_group.add(bullent)


        bullent1 = Bullent()
        bullent1.rect.centerx = self.rect.centerx - 35
        bullent1.rect.y = self.rect.top + 35
        self.bullent_group.add(bullent1)


        bullent2 = Bullent()
        bullent2.rect.centerx = self.rect.centerx + 35
        bullent2.rect.y = self.rect.top + 35
        self.bullent_group.add(bullent2)


class Bullent(GameSprite):
    def __init__(self):
        self.imagename = './images/bullet.png'
        super().__init__(self.imagename,-20)
        
    def __del__(self):
        print('子弹已被销毁..')

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()
        
