import pygame
from MySprite import *
class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,500)
        pygame.time.set_timer(FIRE_BULLENT,100)

    def start_game(self):
        while True:
            self.clock.tick(100)#设置刷新帧数
            self.__event_handler()#事件监听
            self.__check_collide()#碰撞检测
            self.__update_sprites()#更新精灵族
            pygame.display.update()#更新屏幕显示

    def __create_sprites(self):
        bg1 = BackGroundSprite()
        bg2 = BackGroundSprite(True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('敌机出场...')
                enemy = EnemySprite()
                self.enemy_group.add(enemy)

            elif event.type == FIRE_BULLENT:
                self.hero.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 10
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -10
            
        else:
            self.hero.speed = 0
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.hero.speed1 = -10
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed1 = 10
        else:
            self.hero.speed1 = 0
        '''
        if keys_pressed[K_SPACE]:
            print('发射子弹..')
            self.hero.fire()
        '''
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullent_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()




    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullent_group.update()
        self.hero.bullent_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()

if __name__ == '__main__':

    game = PlaneGame()

    game.start_game()


