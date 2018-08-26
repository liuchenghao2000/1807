import pygame
from plane_sprites import *

class PlaneGame(object):
	"""图片大战主游戏"""
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
			# 1. 设置刷新帧率
			self.clock.tick(60)
			# 2. 事件监听（移动触发图片）
			self.__event_handler()
			# 3. 碰撞检测（图片叠加）
			self.__check_collide()
			# 4. 更新精灵组（图片）
			self.__update_sprites()
			# 5. 更新屏幕显示（更新图层）
			pygame.display.update()
	def __create_sprites(self):
		# 背景组
		self.back_group = pygame.sprite.Group()
		# 创建背景精灵和精灵组
		bg1 = Background("./images/background.png")
		bg2 = Background("./images/background.png")
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1, bg2)
		# 敌机组
		self.enemy_group = pygame.sprite.Group()
		# 英雄组
		self.hero_group = pygame.sprite.Group()
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				PlaneGame.__game_over()
	def __check_collide(self):
	def __update_sprites(self):
		for group in [self.back_group, self.enemy_group, self.hero_group]:
		group.update()
		group.draw(self.screen)
	@staticmethod
	def __game_over():
		'''游戏结束'''
		print('游戏结束')
		pygame.quit()
		exit()
if __name__ == '__main__':
	# 创建游戏对象
	game = PlaneGame()

	# 开始游戏
	game.start_game()