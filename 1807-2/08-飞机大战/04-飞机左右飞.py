import pygame
from MySprite import *

pygame.init()

#hero_rect =　pygame.Rect(100,500,120,126)
screen = pygame.display.set_mode((480,700))#创建窗口
bg = pygame.image.load('./images/background.png')#加载背景图
#screen.blit(bg,(0,0))
#pygame.display.update()#更新

hero = pygame.image.load('./images/hero1.png')
screen.blit(hero,(200,500))
#pygame.display.update()
    

#clock = pygame.time.Clock()
#hero_rect = pygame.Rect(200,500,120,126)
 
enemy = EnemySprite()
enemy1 = EnemySprite()
enemy1.rect.x = 200
enemy1.rect.y = 700
enemy1.speed = -2
enemy_group = pygame.sprite.Group(enemy,enemy1)

clock = pygame.time.Clock()
hero_rect = pygame.Rect(200,500,120,126)
while True:
    
    clock.tick(60)
    hero_rect.x -= 1
    if hero_rect.x <= 0:
        hero_rect.x = 480


    pygame.display.update()
    enemy_group.update()

    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    enemy_group.draw(screen)   
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏...')
            pygame.quit()
