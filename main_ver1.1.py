# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:17:24 2022

@author: Anji
"""

import pygame, sys, os

from save_system import load_save

############################ ASSETS DIRECTORY #######################################
assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")
background_dir = os.path.join(assets_dir,"background")
sound_dir = os.path.join(assets_dir, "sounds")
map_dir = os.path.join(assets_dir, "map")



############################ INITIATE PYGAME #######################################
pygame.init()
screen_width = 500
screen_height = 800

pygame.display.set_caption("Task game")
icon_image = pygame.image.load(os.path.join(background_dir, "ghost_icon.jpg"))
pygame.display.set_icon(icon_image)
window_surface = pygame.display.set_mode((screen_width,screen_height))
game_font = pygame.font.Font("Boxy-Bold.ttf", 20)
clock = pygame.time.Clock()
animation_clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 20)

############################ SAVE/LOAD SYSTEM #######################################


save = load_save()


############################ DATA / LISTS #######################################

state_stack = []
data = {'mana': 0,
        'health': 0,
        'stamina': 0}

options = {'sound': 0.1}

############################ IMAGES #######################################


game_background = pygame.image.load(os.path.join(map_dir, "grass.png"))
game_map = pygame.transform.scale(game_background, (1100, screen_height))


menu_background = pygame.image.load(os.path.join(background_dir, "wallpaper5.jpg"))
default_button = pygame.image.load(os.path.join(sprites_dir, "button", "button2.0.png"))
new_default_button = pygame.transform.scale(default_button, (100,80))
hovering_button = pygame.image.load(os.path.join(sprites_dir, "button", "buttonpress2.0.png"))
new_hovering_button = pygame.transform.scale(hovering_button, (100,100))


############################ SOUNDS #######################################

button_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'button_sound.wav'))
button_hover_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'button_hover_sound.wav'))

music_sound = pygame.mixer.music.load(os.path.join(sound_dir, 'music_sound1.mp3'))
pygame.mixer.music.set_volume(options["sound"])



startText = game_font.render("New Game", True, ((0,0,0)))
quitText = game_font.render("Quit", False, ((0,0,0)))
start_text = game_font.render("Welcome Player", True, ((200,150,50)))



############################ PLAYER ASSETS #######################################

idle_1 = pygame.image.load(os.path.join(sprites_dir,"player","standing.png"))
l1 = pygame.image.load(os.path.join(sprites_dir, "player",'l1.png'))
l2 = pygame.image.load(os.path.join(sprites_dir, "player",'l2.png'))
l3 = pygame.image.load(os.path.join(sprites_dir, "player",'l3.png'))
l4 = pygame.image.load(os.path.join(sprites_dir, "player",'l4.png'))


r1 = pygame.image.load(os.path.join(sprites_dir, "player",'r1.png'))
r2 = pygame.image.load(os.path.join(sprites_dir, "player",'r2.png'))
r3 = pygame.image.load(os.path.join(sprites_dir, "player",'r3.png'))
r4 = pygame.image.load(os.path.join(sprites_dir, "player",'r4.png'))


u1 = pygame.image.load(os.path.join(sprites_dir,"player",'u1.png'))
u2 = pygame.image.load(os.path.join(sprites_dir,"player",'u2.png'))
u3 = pygame.image.load(os.path.join(sprites_dir,"player",'u3.png'))
u4 = pygame.image.load(os.path.join(sprites_dir,"player",'u4.png'))


d1 = pygame.image.load(os.path.join(sprites_dir,"player",'d1.png'))
d2 = pygame.image.load(os.path.join(sprites_dir,"player",'d2.png'))
d3 = pygame.image.load(os.path.join(sprites_dir,"player",'d3.png'))
d4 = pygame.image.load(os.path.join(sprites_dir,"player",'d4.png'))

x = 50
y = 10
width = 40
height = 60
vel = 3


left = False
right = False
up = False
down = False
walkCount = 0

############################ BASIC CAT LOADING ANIMATION #######################################
def cat_animation():
    image_sprite = [pygame.image.load(os.path.join(assets_dir, "loading_screen","tile000.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile001.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile002.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile003.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile004.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile005.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile006.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile007.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile008.png")),
                    pygame.image.load(os.path.join(assets_dir, "loading_screen","tile009.png"))]
     
    current_sprite = 0
     
    
    while True:
        
        if current_sprite >= len(image_sprite):
            current_sprite = 0
    
        image = image_sprite[int(current_sprite)]
     
        x = 150
        y = 150
    
    
        window_surface.blit(image, (x, y))
        pygame.display.update()

     
        current_sprite += 0.010
        


############################ CREATING PLAYER CLASS #######################################
class Player():
    def __init__(self, x, y):
        self.char = pygame.transform.scale(idle_1,(45,45))
        
        self.walkLeft = [pygame.transform.scale(l1,(45,45)), 
                        pygame.transform.scale(l2,(45,45)), 
                        pygame.transform.scale(l3,(45,45)), 
                        pygame.transform.scale(l4,(45,45))]
     
       
        self.walkright = [pygame.transform.scale(r1,(45,45)), 
                        pygame.transform.scale(r2,(45,45)), 
                        pygame.transform.scale(r3,(45,45)), 
                        pygame.transform.scale(r4,(45,45))]
        
        self.walkdown = [pygame.transform.scale(d1,(45,45)), 
                        pygame.transform.scale(d2,(45,45)), 
                        pygame.transform.scale(d3,(45,45)), 
                        pygame.transform.scale(d4,(45,45))]
        
        
        self.walkup = [pygame.transform.scale(u1,(45,45)), 
                        pygame.transform.scale(u2,(45,45)), 
                        pygame.transform.scale(u3,(45,45)), 
                        pygame.transform.scale(u4,(45,45))]
        
        #image = self.walkLeft[int(current_sprite)]
        
    def update(self):
        global walkCount
        global x
        
        
        
        
        if walkCount + 1 >= 4:
            walkCount = 0   
        if left:  
            window_surface.blit(self.walkLeft[int(walkCount)], (x,y))
            walkCount += 0.2
        elif right:  
            window_surface.blit(self.walkright[int(walkCount)], (x,y))
            walkCount += 0.2
        elif up:  
            window_surface.blit(self.walkup[int(walkCount)], (x,y))
            walkCount += 0.2
        elif down:  
            window_surface.blit(self.walkdown[int(walkCount)], (x,y))
            walkCount += 0.2                      
        else:
            window_surface.blit(self.char, (x, y))
            walkCount = 0
            
        pygame.display.update()
        
        
    def movement(self):
        global walkCount
        global x
        global y
        global left
        global right
        global up
        global down
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x > vel: 
            x -= vel
            left = True
            right = False
            up = False
            down = False
        elif keys[pygame.K_d] and x < screen_width - vel - width:  
            x += vel
            left = False
            right = True
            up = False
            down = False
        elif keys[pygame.K_w] and y > vel: 
            y -= vel
            up = True
            left = False
            right = False
            down = False
        elif keys[pygame.K_s] and y < screen_height - vel - width: 
            y += vel
            up = False
            left = False
            right = False
            down = True
        else: 
            left = False
            right = False
            up = False
            down = False
            walkCount = 0
player_1 = Player(20,20)   



############################ CREATING BUTTON CLASS #######################################
class Button():
    def __init__(self,x, y, default_image):
        self.default_image = default_image
        self.rect = self.default_image.get_rect(center = (x, y))
        self.click = False
        self.button_hover = False
        
    def update(self):
        pos = pygame.mouse.get_pos()
        action = False
        window_surface.blit(self.default_image, self.rect)
        
        if self.rect.collidepoint(pos):
            self.default_image = new_hovering_button
            
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                button_sound.play()
                self.click = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
                

            if self.rect.collidepoint(pos) == True and self.button_hover == False:
                button_hover_sound.play()
                self.button_hover = True
    


        else:
            self.default_image = new_default_button
            self.button_hover = False
        return action



################################# CREATING EXIT MENU #######################################
def exit_menu():
    run = True
    #menu_button = pygame.transform.scale(new_default_button, (300, 100))
    menu_button1 = Button(310,200, new_default_button)
    menu_text = font.render("Menu", True, ((0,0,0)))
    
    while run:
        
        scaling_menu_surface = pygame.image.load(os.path.join(sprites_dir, "pause", "scroll_menu.png"))
        menu_surface = pygame.transform.scale(scaling_menu_surface, (450,550))
        #menu_surface.fill((255,255,255))
        
        
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (screen_width*.50, screen_height*.5)
        
        
        window_surface.blit(menu_surface, menu_rect)
        window_surface.blit(menu_text, (200,100))
        
        if menu_button1.update():
            Transition_screen(screen_width, screen_height, game_background)
            state_stack[menu()]
        
        
        
        
        window_surface.blit(font.render(str("Health:")+str(data["health"]), True, (200,150,50)), (110, 200))
        window_surface.blit(font.render(str("Mana:")+str(data["mana"]), True, (200,150,50)), (110, 300))
        window_surface.blit(font.render(str("Stamina:")+str(data["stamina"]), True, (200,150,50)), (110, 450))
        pygame.display.update()
        clock.tick(60)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    
                    
################################# CREATING PAUSE MENU #######################################
def pause_menu():
    run = True
    #menu_button = pygame.transform.scale(new_default_button, (300, 100))
    menu_button1 = Button(310,200, new_default_button)
    stats_text = font.render("Status", True, ((200,150,50)))
    
    while run:
        
        scaling_menu_surface = pygame.image.load(os.path.join(sprites_dir, "pause", "ui_1.png"))
        menu_surface = pygame.transform.scale(scaling_menu_surface, (1200,1500))
        #menu_surface.fill((255,255,255))
        
        
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (screen_width*.50, screen_height*.4)
        
        
        window_surface.blit(menu_surface, menu_rect)
        window_surface.blit(stats_text, (200,100))
        
        if menu_button1.update():
            data["mana"] += 1
        
        
        
        
        window_surface.blit(font.render(str("Health:")+str(data["health"]), True, (200,150,50)), (110, 200))
        window_surface.blit(font.render(str("Mana:")+str(data["mana"]), True, (200,150,50)), (110, 300))
        window_surface.blit(font.render(str("Stamina:")+str(data["stamina"]), True, (200,150,50)), (110, 450))
        pygame.display.update()
        clock.tick(60)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    run = False
        
        
################################# DEFAULT FADING TRANISITION #######################################
def Transition_screen(width, height, current_scene):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(190, 300):
        fade.set_alpha(alpha)
        #cat_animation()
        window_surface.blit(current_scene, (0,0))
        window_surface.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(3)
           
        
################################# BASIC SHORT TRANSITION #######################################
def short_transition():
    #transition = pygame.image.load(os.path.join(background_dir, "fading_screen3.jpg"))
    window_surface.fill((255,200,255))
    #window_surface.blit(transition, (0,0))
    pygame.display.update()
    pygame.time.delay(4000)



################################# LOADING IMAGE AT START OF GAME #######################################
def StartUp_screen():
    start_up = pygame.image.load(os.path.join(background_dir, "wallpaper1.jpg")).convert_alpha()
    window_surface.blit(start_up, (0,0))
    window_surface.blit(start_text, (100,350))
    
    pygame.display.update()
    pygame.time.delay(3000)


################################# MENU SCREEN #######################################
def menu():
    pygame.mixer.music.play(-1)
    
    
    #music_sound.pause()
    
    running = True
    button_1 = Button(100, 650, new_default_button)
    button_2 = Button(250, 650, new_default_button)
    button_3 = Button(400, 650, new_default_button)
    
    
    menu_background = pygame.image.load(os.path.join(background_dir, "wallpaper5.jpg"))
    
    while running:
         
         window_surface.blit(menu_background, (0,0))
         
         #redraw_menu_window()
         
         if button_1.update():
             pygame.mixer.music.fadeout(1000)
             Transition_screen(screen_width, screen_height, menu_background)
        
             state_stack.append(game_scene())
             state_stack[game_scene()]
             
         if button_2.update():
             pygame.mixer.music.fadeout(1000)
             Transition_screen(screen_width, screen_height, menu_background)
             state_stack.append(load_scene())
             state_stack[load_scene()]
             
             
         if button_3.update():
             pygame.mixer.music.fadeout(1000)
             pygame.quit()
             sys.exit()
             
         #window_surface.blit(startText, (540, 350))
         #window_surface.blit(quitText, (590, 585))
         pygame.display.update()
         clock.tick(60)
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
        
        
        
################################# OPTIONS SCREEN / LOAD SCREEN TEMP #######################################
def load_scene():
    
    
    running = True
    options_button_1 = Button(250, 150, new_default_button)
    options_button_2 = Button(370, 150, new_default_button)
    
    
    load_game_background = pygame.image.load(os.path.join(background_dir, "town.png"))
    #load_game_background = pygame.transform.scale(scaling_load_game_background, (500,800))
    while running:
        window_surface.blit(load_game_background, (0,0))
        
        
        if options_button_1.update():
            options["sound"] -= 0.1
            
        if options_button_2.update():
            options["sound"] += 0.1
        

        
        
        
        
        window_surface.blit(font.render(str("Sound Level:")+str(options["sound"]), True, (255, 255, 255)), (32, 48))
            
        pygame.display.update()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Transition_screen(screen_width, screen_height, load_game_background)
                    #state_stack.load_scene().pop()
                    
                    state_stack[menu()]




################################# GAME / MAIN SCREEN #######################################
def game_scene():
    
    
    running = True
    
    while running:
        
        window_surface.blit(game_map, (0,0))
        
        player_1.update()
        player_1.movement()
        pygame.display.update()
        
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #Transition_screen(screen_width, screen_height, game_background)
                    #state_stack[menu()]
                    exit_menu()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_menu()
        
        
        
        
################################# CREATING COUNTDOWN TIMER FUNCTION #######################################       
def CountDown_timer():
    counter = 650
    text = 'starting'.rjust(17)
    
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    load_game_background = pygame.image.load(os.path.join(background_dir, "load_scene.jpg"))
    font = pygame.font.SysFont('Consolas', 30)
    run = True
    while run:
        sec =   counter-(60*(60)) #seconds left
        hour = (counter// 3600) # hours left
        sec %= 3600
        min = sec // 60 # minutes left
        day = (counter // 86400) 
        if hour >= 24 and min >= 0:
            hour = hour - (24*day)
        sec %= 60
        
        
        
     
            
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter -= 1
                
                if counter > 0:
                    #text = str(counter).rjust(3)
                    text = ("Time remaining: "+str(day)+":"+str(hour)+":"+str(min)+":"+str(sec))
                    if sec < 10:
                        text = ("Time remaining: "+str(day)+":"+str(hour)+":"+str(min)+":"+"0"+str(sec))
                        if sec < 10 and min < 10:
                            text = ("Time remaining: "+str(day)+":"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                            if sec < 10 and min < 10 and hour < 10:
                                text = ("Time remaining: "+str(day)+":"+"0"+":"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                                if sec < 10 and min < 10 and hour < 10 and day < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+":"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                    if min < 10:
                        text = ("Time remaining: "+str(day)+":"+str(hour)+":"+"0"+str(min)+":"+str(sec))
                        if min < 10 and sec < 10:
                            text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                            if min < 10 and hour < 10 and sec < 10:
                                text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                                if min < 10 and hour < 10 and sec < 10 and day < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                                
                            
                    if hour < 10:
                        text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+str(min)+":"+str(sec))
                        if hour < 10 and min < 10:
                            text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+str(sec))
                            if hour < 10 and min < 10 and sec < 10:
                                text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                                if hour < 10 and day < 10 and min < 10 and sec < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
                    if day < 10:
                        text = ("Time remaining: "+"0"+str(day)+":"+str(hour)+":"+str(min)+":"+str(sec))
                        if day < 10 and hour < 10:
                            text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+str(min)+":"+str(sec))
                            if day < 10 and hour < 10 and min < 10:
                                text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+str(sec))
                                if day < 10 and hour < 10 and min < 10 and sec < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(min)+":"+"0"+str(sec))
    
                else: 
                    text = str('boom!')
                
                
            if e.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                
                
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    Transition_screen(1280, 720, load_game_background)
                    
                    state_stack[menu()]
        
        new_surface = pygame.Surface((490, 50))
        new_surface.fill((255, 255, 255))
        #window_surface.fill((255,200,255))
        window_surface.blit(new_surface, (10,30))
        window_surface.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        
        
        


  
        
################################# CALLING MENU SCREEN #######################################
if __name__ == "__main__":
    StartUp_screen()
    menu()
    
    
    
    