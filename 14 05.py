import pygame as pg
import sys
from sky import Sky
from settings import *
import random
from meteor import Meteor
pg.init()
screen= pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
sky = Sky("sky.png",screen , x,y) 
if player.hp >= 0:
    print('GAME OVER')


player_hits_bonuses = pygame.sprite.spritecollide(player, bonuses, True, pygame.sprite.collide_circle)
for hit in player_hits_bonuses:
    if hit.type == 'hp':
        player.hp += random.randint(20, 50)
        if player.hp > 100:
            player.hp = 100
        elif hit.type == 'gun':
            player.gun.bonus = True
            player.gun_bonus_timer = pygame.time.get_ticks()
        elif hit.type == 'shield':
            shield = shield

    

while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()



                if plauer.gun_bonus:
                    bullet = Bullet(player.rect.centerx, player.rect.midright)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
sky1 = Sky('sky.png',screen,(SCREEN_WIDTH - 200) // 2,0)
sky2 = Sky('sky.png',screen,(SCREEN_WIDTH - 200) // 2, - SCREEN_HEIGHT)

sky.update()
screen_fill((0,0,0))
pg.display.update()
