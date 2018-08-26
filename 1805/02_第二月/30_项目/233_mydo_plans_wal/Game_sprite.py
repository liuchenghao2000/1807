import pygame
#精灵
SCREEN_RECT=pygame.rect(0,0,480,800)

class Game_sprite():
	""" Base for Game_sprite"""
	def __init__(self,image,speed=1):
		super().__init__()
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		self.speed=speed
	def update(self,*args):
		self.rect.y+=self.speed
class BkGd_sprite(Game_sprite):
	"""sprite for BackGround"""
	def __init__():
		image=''
		super().__init__(image,speed=1)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self,*args):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height		
class Enemy_sprite(Game_sprite):
	"""sprite for Enemy"""
	def __init__():
		image=''
		super().__init__(image,speed=2)
	def update(self,*args):
		super().update()
class  Hero_sprite(Game_sprite):
	"""sprite for Hero"""
	def __init__():
		image=''
		super().__init__(image)
	def update(self,*args):
		super().update()
		if self.rect.left<=0:
			self.rect.left=0
		if self.rect.right>=SCREEN_RECT.width:
			self.rect.right=SCREEN_RECT.width
class Bill_sprite(Game_sprite):
	"""sprite for B"""
	def __init__():
		image=''
		super().update()
	def update(self,*args):
		super().update()


