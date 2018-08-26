#框架
import pygame
from sprites import *
class Plan_wal(object):
		'''飞机大战主游戏'''
	def __init__(self):
		'''游戏初始化'''

		self.sereen=pygame.display.set_mode(SCREEN_RECT.size)#屏幕
		self.pygame.time.Clock()#时钟
		self.__create_sprites()#精灵组
	def Start_Game(self):
		'''开始游戏'''
		print('开始游戏...')
		while True:
			self.Clock.tike(60)
			self.__Event_hardler(self)
			self.__check_collide(self)
			self.__UpDate_sprites()
			self.
			self.
	def __Evenet_Key(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over
	def __Check_collide(self):

	def __Screen(self):
		self.pygame.display.update() 更新屏幕显示
	def __UpDate_Srites(self):

	def __Game_over(self):

