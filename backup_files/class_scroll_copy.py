

import pygame,os,sys
from pygame.math import Vector2
        

    
class Scroll(object):
    def __init__(self, window_surface, screen_width, screen_height, state_stack, game_scene, stats):
        assets_dir = os.path.join("assets")
        sprites_dir = os.path.join(assets_dir, "sprites")

        self.text_height = 50
        self.text_default_height = 0
        self.text_colour = (200,150,50)


        self.max_scroll_height_top = 270
        self.max_scroll_height_bottom = 100


        self.stats = stats

        self.screen_width = screen_width
        self.screen_height = screen_height


        self.default_button = pygame.image.load(os.path.join(sprites_dir, "button", "button2.0.png"))
        self.new_default_button = pygame.transform.scale(self.default_button, (100,80))

        self.hovering_button = pygame.image.load(os.path.join(sprites_dir, "button", "buttonpress2.0.png"))
        self.new_hovering_button = pygame.transform.scale(self.hovering_button, (100,100))
        
        self.positon_cord = (self.screen_width*.5, 270)
        self.position = Vector2((self.positon_cord))

        
        
        self.state_stack = state_stack
        self.game_scene = game_scene
        
        self.font = pygame.font.SysFont('Consolas', 20)
        
        #self.sub = window_surface.subsurface((120,0,300,150)).copy()
        #self.sub.fill((200,150,50))
        
        
        
        self.background_surface = pygame.image.load(os.path.join(sprites_dir, "pause", "scrolling_bg.png"))
        self.background = pygame.transform.scale(self.background_surface, (400,250))
        
        self.Quest_panal_scale = pygame.image.load(os.path.join(sprites_dir, "pause", "quest_panal.png"))
        self.Quest_panal = pygame.transform.scale(self.Quest_panal_scale, (270, 30))
        
        self.frame_img_scale = pygame.image.load(os.path.join(sprites_dir, "pause", "scrolling_frame.png"))
        self.frame_img = pygame.transform.scale(self.frame_img_scale, (300,150))
        
        self.stats_text = self.font.render("QUEST", True, self.text_colour)
        self.exp_text = self.font.render(str("exp:")+str(self.stats["curr_exp"]), True, self.text_colour)
        self.level_text = self.font.render(str("Lv:")+str(self.stats["exp_level"]), True, self.text_colour)
        self.name_text = self.font.render(str("NAME:")+str("???"), True, self.text_colour)  
        self.job_text = self.font.render(str("JOB:")+str("???"), True, self.text_colour)  
        self.title_text = self.font.render(str("TITLE:")+str("???"), True, self.text_colour) 


        # // button //
        self.default_image = self.new_default_button
        self.hovering_image = self.new_hovering_button
        self.current_image = self.new_default_button
        self.window_surface = window_surface
        
        self.click = False
        
        self.button_hover = False
        
        self.rect = self.Quest_panal.get_rect(center=(self.positon_cord))
        self.hitbox = self.rect.inflate(0, 0)
        self.display_button = True
        self.quest_box_size = (300,150)
        self.quest_box_surface = pygame.Surface((self.quest_box_size))
        self.quest_box_rect = self.quest_box_surface.get_rect()
        self.quest_box_rect.x = 150
        self.quest_box_rect.y = 250
        self.quest_box_surface.fill((255,255,255))
        
    def update_button(self, pos_y):
        
       
        
        if self.display_button:
            pos = pygame.mouse.get_pos()
            action = False
            self.rect.center = self.position 
            self.hitbox.center = self.position 
            
            self.rect.y = self.rect.y + pos_y
            self.hitbox.y = self.hitbox.y + pos_y
            
            #pygame.draw.rect(self.window_surface, (0, 230, 0), self.rect, 2)
            #pygame.draw.rect(self.window_surface, (250, 30, 0), self.hitbox, 2)
            self.window_surface.blit(self.Quest_panal, (self.rect.x, self.rect.y))
            
            if self.hitbox.collidepoint(pos):
                self.current_image = self.hovering_image
                
                if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                    #button_sound.play()
                    self.click = True
                    action = True
                    
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click = False
                    

                if self.hitbox.collidepoint(pos) == True and self.button_hover == False:
                    #button_hover_sound.play()
                    self.button_hover = True
        


            else:
                self.current_image = self.default_image
                self.button_hover = False
            return action  

       
          
        
    def update_event(self, window_surface):
        self.window_surface.blit(self.quest_box_surface, (self.quest_box_rect))
        #self.draw_text(window_surface)
    
        if self.update_button(0):
            print("button 1 working")

        if self.update_button(50):
            print("button 2 working")

        if self.update_button(100):
            print("button 3 working")

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            ########################### // Scrolling boundries // ##############################
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 4:
                    print("4", self.position.y)
                    

                    
                    if self.position.y  == self.max_scroll_height_top:
                        self.position.y += 0
                
                    elif self.position.y  == self.max_scroll_height_bottom:
                        self.position.y += 10
                    
                    else:
                        
                        self.position.y += 10
                        
                    #if self.rect.y <= 150:
                    #    self.display_button = False
                    
                    #else:
                    #    self.display_button = True





                    


                if e.button == 5:
                    print("5", self.position.y)

                    
                        
                    

                    if self.position.y  == self.max_scroll_height_top:
                        
                        self.position.y -= 10
                        
            
                    elif self.position.y == self.max_scroll_height_bottom:
                        self.position.y -= 0
                    
                    else:
                        self.position.y -= 10
                    
                        
                    

                    #if self.rect.y >= -150:
                    #    self.display_button = False
                    
                    #else:
                    #    self.display_button = True



                    
            
            ########################### // Scrolling boundries // ##############################
            
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.text_height -= 5
                    
                    
                if e.key == pygame.K_DOWN:
                    self.text_height += 5
            
                if e.key == pygame.K_q:
                    #game_sound.play(-1)
                    self.state_stack[self.game_scene()]
                       
        #pygame.display.update()           
    #def draw_text(self, window_surface):
        
        
    #    self.sub.blit(self.background, (0,0))
        
        #self.sub.blit(self.Quest_panal,  (self.screen_width*.03,self.text_height))
        #self.sub.blit(self.Quest_panal,  (self.screen_width*.03,self.text_height+ self.screen_height*.05))
        #self.sub.blit(self.Quest_panal,  (self.screen_width*.03,self.text_height+ self.screen_height*.1))
        
        #self.sub.blit(self.Quest_panal,  (self.screen_width*.03,self.text_height+ self.screen_height*.15))
    #    self.sub.blit(self.Quest_panal, (self.position.x, self.position.y))
    #    self.sub.blit(self.Quest_panal,  (self.screen_width*.03,self.text_height+ self.screen_height*.2))
    #    self.sub.blit(self.Quest_panal,  (self.screen_width*.03,self.text_height+ self.screen_height*.25))
            
    #    window_surface.blit(self.sub, (155,250))
    #    window_surface.blit(self.frame_img, (155,250))