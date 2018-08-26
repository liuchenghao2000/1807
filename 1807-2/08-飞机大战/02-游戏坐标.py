import pygame

pygame.init()

#hero_rect =　pygame.Rect(100,500,120,126)
screen = pygame.display.set_mode((480,700))#创建窗口
bg = pygame.image.load('./images/background.png')#加载背景图
screen.blit(bg,(0,0))
pygame.display.update()#更新

hero = pygame.image.load('./images/hero1.png')
screen.blit(hero,(200,500))
pygame.display.update()
    

clock = pygame.time.Clock()
hero_rect = pygame.Rect(200,500,120,126) 
while True:
    
    clock.tick(60)
    hero_rect.y -= 5
    if hero_rect.y <= 0:
        hero_rect.y = 700


    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    pygame.display.update()
    


pygame.quit()
