# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:06:11 2022

@author: Noatok
"""

import pygame, sys


pygame.init()

game_surface = pygame.Surface((400,400))
screen = pygame.display.set_mode((500,800), pygame.RESIZABLE)
clock = pygame.time.Clock()


running = True

while running:
    screen.fill((200,150,50))
    screen.blit(game_surface, (200,0))
    pygame.display.update()
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if e.type == pygame.VIDEORESIZE:
            game_surface = pygame.Surface((e.w,e.h), pygame.RESIZABLE)
