import pygame
from plane_sprites import *


class PlaneGame(object):
	"""飞机大战主游戏"""

	def __init__(self):#时间地点人
		print("游戏初始化")
		# 1. 创建游戏的窗口
		self.screen = pygame.display.set_mode((480, 700))
		# 2. 创建游戏的时钟
		self.clock = pygame.time.Clock()
		# 3. 调用私有方法，精灵和精灵组的创建
		self.__create_sprites()

	def start_game(self):
		print("开始游戏...")
		while True:
			pass
	def __create_sprites(self):
		pass

		
if __name__ == '__main__':
	# 创建游戏对象
	game = PlaneGame()

	# 开始游戏
	game.start_game()