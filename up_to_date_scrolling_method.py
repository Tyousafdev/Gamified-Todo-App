# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:40:43 2022

@author: Noatok
"""

import pygame,sys, os

pygame.init()
font = pygame.font.SysFont('Consolas', 20)
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255,255,255))
sub = screen.subsurface((0,0,400,200)).copy()
sub.fill((200,150,50))
fps = pygame.time.Clock()

#############################################################
assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")
background_dir = os.path.join(assets_dir,"background")
sound_dir = os.path.join(assets_dir, "sounds")
map_dir = os.path.join(assets_dir, "map")
font_dir = os.path.join(assets_dir, "font")


######################### TEXT ###############################
text_sample = font.render("test", True, ((255,255,255)))

text_colour = (255,255,255)
stats = {'mana': 0,
            'health': 0,
            'stamina': 0,
            'curr_exp': 0,
            'exp_points_limit': 150,
            'exp_level': 0}   

background_surface = pygame.image.load(os.path.join(sprites_dir, "pause", "scrolling_bg.png"))
Quest_panal_scale = pygame.image.load(os.path.join(sprites_dir, "pause", "quest_panal.png"))
Quest_panal = pygame.transform.scale(Quest_panal_scale, (350, 30))
    
background = pygame.transform.scale(background_surface, (400,250))
stats_text = font.render("Status", True, text_colour)

exp_text = font.render(str("exp:")+str(stats["curr_exp"]), True, text_colour)
level_text = font.render(str("Lv:")+str(stats["exp_level"]), True, text_colour)
name_text = font.render(str("NAME:")+str("???"), True, text_colour)  
job_text = font.render(str("JOB:")+str("???"), True, text_colour)  
title_text = font.render(str("TITLE:")+str("???"), True, text_colour)










text_height = 50

max_scroll_height_top = 50
max_scroll_height_bottom = -350
pygame.display.update()

while True:
    sub.blit(background, (0,0))
    sub.blit(Quest_panal,  (screen_width*.05,text_height))
    sub.blit(Quest_panal,  (screen_width*.05,text_height+screen_height*.1))
    sub.blit(Quest_panal,  (screen_width*.05,text_height+screen_height*.2))
    sub.blit(Quest_panal,  (screen_width*.05,text_height+screen_height*.3))
    sub.blit(Quest_panal,  (screen_width*.05,text_height+screen_height*.4))
    sub.blit(Quest_panal,  (screen_width*.05,text_height+screen_height*.5))
    screen.blit(sub, (30,40))
    
    
    
    
    
    
    
    
    pygame.display.flip()
    fps.tick(120)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        ########################### // Scrolling boundries // ##############################
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 4:
                if text_height == max_scroll_height_top:
                    text_height += 0
                elif text_height == max_scroll_height_bottom:
                     text_height += 10
                else:
                    text_height += 10
                
            if e.button == 5:
                if text_height == max_scroll_height_top:
                    text_height -= 10
        
                elif text_height <= max_scroll_height_bottom:
                     text_height -= 0
                else:
                    text_height -= 10
                    
        ########################### // Scrolling boundries // ##############################
        
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                
                sub.fill((200,150,50))
                screen.blit(sub, (30,40))
                
                
                text_height -= 5
            if e.key == pygame.K_DOWN:
                sub.fill((200,150,50))
                
                screen.blit(sub, (30,40))
                
                
                text_height += 5


class Scroll(object):
    def __init__(self):
        pass
    def check_events(self):
        pass
    def draw_text(self):
        pass