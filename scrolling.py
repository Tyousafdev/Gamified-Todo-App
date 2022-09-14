# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:16:42 2022

@author: Noatok
"""

import pygame, sys, os
import string

pygame.init()
assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")

screen = pygame.display.set_mode((500, 800))
panal_img = pygame.image.load(os.path.join(sprites_dir, "pause", "stats_ui.png"))
panal = pygame.transform.scale(panal_img, (1200,1500))
pygame_surface = pygame.surface.Surface((200, 200))
pygame_surface.fill((200,150,50))

surface_rect = pygame_surface.get_rect()

y = 20
font = pygame.font.SysFont('', 25)

data = {'name': "Talha",
        'job': "???",
        'Title': "???",
        'HP': 1,
        "MP": 3}

text1 = "NAME"
text2 = "JOB"
text3 = "TITLE"
text4 = "HP"
text5 = "MP"
text6 = "FATIGUE"

pygame_surface.blit(font.render(str(data["name"]), True, (255, 255, 255)), (50, y))
pygame_surface.blit(font.render(str(data["job"]), True, (255, 255, 255)), (50, y+40))
pygame_surface.blit(font.render(str(data["Title"]), True, (255, 255, 255)), (50, y+80))
pygame_surface.blit(font.render(str(data["HP"]), True, (255, 255, 255)), (50, y+120))
pygame_surface.blit(font.render(str(data["MP"]), True, (255, 255, 255)), (50, y+140))
pygame_surface.blit(font.render(text6, True, (255, 255, 255)), (50, y+180))


clock = pygame.time.Clock()    
#quit = False

scroll_y = 0
run = True
while run:
    pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        
        if surface_rect.collidepoint(pos):
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4: 
                    scroll_y = min(scroll_y + 15, 0)
                    
                if e.button == 5: 
                    scroll_y = max(scroll_y - 15, -300)
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
    #screen.blit(panal,(-350,-350))
    screen.blit(pygame_surface, (0, scroll_y))
    pygame.display.flip()
    clock.tick(60)