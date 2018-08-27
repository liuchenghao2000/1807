import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60 # 刷新帧率
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_BULLET_EVENT = pygame.USEREVENT+1# 英雄发射子弹事件
#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy0_down1.png')
bg2 = pygame.image.load('./images/enemy0_down2.png')
bg3 = pygame.image.load('./images/enemy0_down3.png')
bg4 = pygame.image.load('./images/enemy0_down4.png')
#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()
#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):#父类 大写
    def __init__(self,image,speed=1):
        super().__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y +=self.speed
class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt = False):
        imagename = "./images/background.png"
        super().__init__(imagename,1)
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 1. 调用父类的方法实现
        super().update()
        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
        super().__init__("./images/enemy-1.gif")
        # 2. 设置敌机的随机初始速度
        self.speed = random.randint(1,3)
        # 3. 设置敌机的随机初始位置
        max = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max)
        self.rect.bottom = 0
        self.down_index = 0 #敌机销毁图片索引
    def update(self):
        # 1. 调用父类方法，让敌机在垂直方向运动
        super().update()
        # 2. 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
class Hero(GameSprite):

    """英雄精灵"""

    def __init__(self):

        super().__init__("./images/hero1.png", 0)

        #创建子弹组
        self.bullet_group = pygame.sprite.Group()
        # 设置初始位置
        self.rect.center = SCREEN_RECT.center
        self.rect.bottom = SCREEN_RECT.bottom - 40
    def update(self):
        #飞机水平移动
        self.rect.x += self.speed
        self.rect.y += self.speed1
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
    def fire(self):
        bullet = BulletSprite()#子弹精灵组
        bullet.rect.x = self.rect.centerx
        bullet.rect.bottom = self.rect.top
        bullet1 = BulletSprite()
        bullet1.rect.x = self.rect.centerx - 35
        bullet1.rect.bottom = self.rect.top+30
        bullet2 = BulletSprite()
        bullet2.rect.x = self.rect.centerx + 35
        bullet2.rect.bottom = self.rect.top + 30
        self.bullet_group.add(bullet)
        self.bullet_group.add(bullet1)
        self.bullet_group.add(bullet2)
class BulletSprite(GameSprite): #创建子弹精灵
    def __init__(self):
        imagename = "./images/bullet.png"
        super().__init__(imagename,-10)
    def update(self):
        super().update()
        # 判断是否超出屏幕，如果是，从精灵组删除

        if self.rect.bottom < 0:

            self.kill()
class Soruce(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()
