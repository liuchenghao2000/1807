import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)#常量
class GameSprite(pygame.sprite.Sprite):#父类 大写

    def __init__(self,image,speed=1):
        super().__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y +=self.speed