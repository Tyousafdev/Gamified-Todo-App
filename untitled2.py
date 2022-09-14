# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:31:44 2022

@author: Noatok
"""
import pygame,sys
pygame.init()
windowSurface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

# raise the USEREVENT every 1000ms


pygame.time.set_timer(pygame.USEREVENT, 200)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
string = "A long time ago"
windowSurface.fill((0,0,0))
for i in range(len(string)):
    text = font.render(string[i], True, (0, 128, 0))
    windowSurface.blit(text,(400 + (font.size(string[:i])[0]), 300))
    pygame.display.update()
    clock.tick(2)
    
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()