import pygame
pygame.init()

creen = pygame.display.set_mode((480, 700))

#绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")

# 2> 绘制在屏幕
screen.blit(bg, (0, 0))

# 3> 更新显示
pygame.display.update()

while True:
	pass
pygame.init()
