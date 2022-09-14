# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:38:09 2022

@author: Noatok
"""

import pygame, os, sys
from pygame.locals import*

screen_surface = pygame.Surface((600,600))
screen = pygame.display.set_mode((1250,720))
pygame.init()
clock=pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 20)
bg_x = 500
bg_y = 200

boxx=200
boxy= bg_y

assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")
sprites_dir = os.path.join(assets_dir, "sprites")
background = pygame.image.load(os.path.join(sprites_dir, "panal", "Stats_ui_3_0.png")) 


background_surface = pygame.transform.scale(background, (500,500))
background_surface_rect = background_surface.get_rect()

print(background_surface_rect.bottom)


#image = pygame.Surface([100,100]).convert_alpha()
#image.fill((255,255,255))


image = font.render(str("JOB:")+str("???"), True, (0,0,0))
image2 = font.render(str("NAME:")+str("???"), True, (0,0,0))
speed = 5   # larger values will move objects faster
while True :
    screen.fill((255,150,0))
    screen.blit(background_surface, (bg_x,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        boxy -= 3
    if keys[pygame.K_DOWN]:
        boxy += 3
        
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                boxy -= 7
                    
            elif event.button == 5:
                boxy += 7
        
    #image.scroll(10,10)
    # I did modulus 720, the surface width, so it doesn't go off screen
    screen.blit(image,(bg_x+10, (boxy-100) % background_surface_rect.bottom))
    screen.blit(image2,(bg_x+100, (boxy+100) % background_surface_rect.bottom))
    pygame.display.update()
    clock.tick(60)