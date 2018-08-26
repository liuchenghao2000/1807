import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)#游戏屏幕大小
#基类
class GameSprite(pygame.sprite.Sprite):
	'''游戏精灵基类'''
	def __init__(self,image_name,speed=1):
		super().__init__()							#调用父类
		self.image=pygame.image.load(image_name)	#引用图片
		self.rect=self.image.get_rect()				#应用
		self.speed=speed							#移动速度
	def update(self,*args):
		self.rect.y+=self.speed				#默认在垂直方向移动
#背景精灵
class BackGround(GameSprite):
	def __init__(self,image_name,is_alt = False):
		imagename = './images/bullet-1.gif'
		super().__init__(imagename,100)
		if is_alt:
			self.rect.y= -self.rect.height
	def BackGroundSprite(self):
		super().update()
		if self.rect.y>=SCREEN_RECT.height:
			self.rect.y = -self.rect.height
#敌机精灵
class Enemy_Sprite(GameSprite):
	def __init__(self,image_name):
		imagename = './images/enemy0.png'
		super().__init__(imagename,200)
	def Enemy_Sprite(self):
		super().update()
'''
#弹药精灵
class Ammo(GameSprite,is_alt=Flase):
	def __init__(self,image_name):
		#self.image=pygame.image.load(image_name)
		imagename = './images/background.png'
		super().__init__(imagename,100)
		if is_alt:
			self.rect.y= -self.rect.height

	def BackGroundSprite(self):
		super().update()
		if self.rect.y>=SCREEN_RECT.height:
			self.rect.y = -self.rect.height
'''
'''
#1) 导入 plane_sprites 模块
from plane_sprites import * 
#2) 修改初始化部分代码

# 创建敌机精灵和精灵组
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
enemy2.rect.x = 200
enemy_group = pygame.sprite.Group(enemy1, enemy2)
'''