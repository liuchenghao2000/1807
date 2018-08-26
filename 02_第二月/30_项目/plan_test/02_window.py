#creat window
import pygame
pygame.init()
#窗口
#set_mode(resolution=(0,0),flags=0,depth=0)->Surface
screen = pygame.display.set_mode((480,700))
background=pygame.image.load('./images/background.png')

while True:
	screen.blit(background,(0,0))
	pygame.display.update()



pygame.quit()