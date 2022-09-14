# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:09:59 2022

@author: Noatok
"""

import pygame, sys, os


pygame.init()

screen_width = 500
screen_height = 800
window_display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont('Consolas', 20)
algard_font = pygame.font.Font("alagard.ttf", 40)


assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")

def Main():
    running = True
    
    while running:
        window_display.fill((255,255,255))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Pause()
                

def Pause():
    run = True
    #menu_button = pygame.transform.scale(new_default_button, (300, 100))
    
    stats_text = font.render("Status", True, ((200,150,50)))
    
    while run:
        
        scaling_menu_surface = pygame.image.load(os.path.join(sprites_dir, "panal", "Stats_ui_3_0.png"))
        menu_surface = pygame.transform.scale(scaling_menu_surface, (450,600))
        #menu_surface.fill((255,255,255))
        
        
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (screen_width*.50, screen_height*.5)
        
        
        window_display.blit(menu_surface, menu_rect)
        window_display.blit(stats_text, (210,170))
        
      
            
     
       
        pygame.display.update()
        clock.tick(60)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
        
if __name__ == "__main__":
    Main()