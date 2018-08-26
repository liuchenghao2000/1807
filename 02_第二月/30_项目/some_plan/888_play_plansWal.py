import pygame			#导入模块以及进入
pygame.init()			#init进入
#设置屏幕属性 resolution:屏幕宽高	flags:显示模式	depth:颜色位数
#pygame.display.set_mode(resolution=(0,0), flags=0, depth=0)# -> Surface
#创建游戏主窗口
screen = pygame.display.set_mode((480, 700))
#设置游戏时钟对象
clock = pygame.time.Clock()
i = 0
#1) 导入 plane_sprites 模块
#from 01_emeny_plan import * 

#游戏循环
while True:
	#设置刷新
	clock.tick(60)
	#绘制背景图像
	bg = pygame.image.load("./images/background.png")
	screen.blit(bg,(0,0))
	#绘制英雄图像
	hero = pygame.image.load("./images/hero1.png")
	screen.blit(hero,(200,500))
	#精灵组
	enemy1 = GameSprite("./images/enemy1.png")
	enemy2 = GameSprite("./images/enemy1.png", 2)
	enemy2.rect.x = 200
	enemy_group = pygame.sprite.Group(enemy1, enemy2)
	#监听
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print('退出游戏')
			pygame.quit()
			exit()
	#更新显示
	pygame.display.update()
#退出模块
