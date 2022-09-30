# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:17:24 2022

@author: Anji
"""

import pygame, sys, os, json


from save_system import write_save
from save_system import create_save
#from class_scroll import Scroll
from Scroll_Class import Scroll

############################ FUTURE PATCHES #############################################
# for resizable options make the main screen a surface and a another window screen 
# // like game_width/game_height and window_width/window_height

# SOON
# > try to implement screen_width and screen_height to sizes for all images // 
#   // so it doesnt matter what resoluation we set the game at + dont have  // 
#   // change every size value when changing screen size 

# > *new loading screen // lofi girl
# > *new button sounds
# > *tidy up exit menu
# > *make short animations for loading/leveling up/messages ect
# > *pause menu music

############################ ASSETS DIRECTORY #######################################
assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")
background_dir = os.path.join(assets_dir,"background")
sound_dir = os.path.join(assets_dir, "sounds")
map_dir = os.path.join(assets_dir, "map")
font_dir = os.path.join(assets_dir, "font")


############################ INITIATE PYGAME #######################################
pygame.init()
#screen_width = 500
#screen_height = 800

screen_width = 608
screen_height = 900


pygame.display.set_caption("Task game")
icon_image = pygame.image.load(os.path.join(background_dir, "ghost_icon.jpg"))
pygame.display.set_icon(icon_image)
window_surface = pygame.display.set_mode((screen_width,screen_height))
game_font = pygame.font.Font("Boxy-Bold.ttf", 20)
clock = pygame.time.Clock()
animation_clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 20)
algard_font = pygame.font.Font("alagard.ttf", 40)
title_algard_font = pygame.font.Font("alagard.ttf", 75)



############################ DATA / LISTS #######################################

state_stack = []
stats = {'mana': 0,
        'health': 0,
        'stamina': 0,
        'curr_exp': 0,
        'exp_points_limit': 150,
        'exp_level': 0}

User_Info = {}
options = {'sound': 0.3}


############################ SAVE/LOAD SYSTEM #######################################



try:
    with open(os.path.join('save.json'), 'r+') as file:
        stats = json.load(file)
    
except:
    save = create_save()
    write_save(save)   



############################ IMAGES #######################################


game_background = pygame.image.load(os.path.join(map_dir, "grass.png"))
game_map = pygame.transform.scale(game_background, (1100, screen_height))


test_object = pygame.image.load(os.path.join(map_dir, "tree.png"))
#test_object_rect = test_object.get_rect()

test_object = pygame.Surface((128,128))
test_object.fill((200,150,50))
test_object_rect = test_object.get_rect()
test_object_rect.center = (300,400)

obstacle = pygame.Rect(400,200, 80,80)


menu_background = pygame.image.load(os.path.join(background_dir, "wallpaper5.jpg"))



############################ BUTTONS ######################################


# RECTANGLE BUTTONS
default_button = pygame.image.load(os.path.join(sprites_dir, "button", "button2.0.png"))
new_default_button = pygame.transform.scale(default_button, (100,80))

hovering_button = pygame.image.load(os.path.join(sprites_dir, "button", "buttonpress2.0.png"))
new_hovering_button = pygame.transform.scale(hovering_button, (100,100))


# MENU TABS
default_tab = pygame.image.load(os.path.join(sprites_dir, "button", "new_tab_unselected.png"))
new_default_tab = pygame.transform.scale(default_tab, (70,60))

hovering_tab = pygame.image.load(os.path.join(sprites_dir, "button", "new_tab_selected.png"))
new_hovering_tab = pygame.transform.scale(hovering_tab, (70,60))

new_hovering_tab_get_rect = pygame.transform.scale(hovering_tab, (70,60))
new_hovering_tab_get_rect2 = pygame.transform.scale(hovering_tab, (70,60))





############################ SOUNDS #######################################

button_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'LoL_HoverClickSound_ver4.mp3'))

button_hover_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'LoL_HoverSound_ver3.mp3'))

game_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'wending.wav'))

music_sound = pygame.mixer.music.load(os.path.join(sound_dir, 'menu1.wav'))

menu_pop_up_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'menu_pop_up.wav'))

bubble_pop_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'bubble_sound.wav'))

level_up_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'task_complete.wav'))


pygame.mixer.music.set_volume(options["sound"])



startText = game_font.render("New Game", True, ((0,0,0)))
quitText = game_font.render("Quit", False, ((0,0,0)))
start_text = algard_font.render("Welcome Player", False, ((200,150,50)))



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


#vel = 3


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
     
    running = True
    while running:
        
        if current_sprite >= len(image_sprite):
            current_sprite = 0
    
        image = image_sprite[int(current_sprite)]
     
        x = 150
        y = 150
    
    
        window_surface.blit(image, (x, y))
        pygame.display.update()

        surface = pygame.Surface((300,300), 0, window_surface)
        surface.fill((255,255,255))
        window_surface.blit(surface, (170,y))
        current_sprite += 0.004
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_e:
                    running = False
                    
############################ CREATING object CLASS #######################################
class obj(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join(map_dir, "tree.png"))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        

    def update(self):
        window_surface.blit(self.image, self.rect)
    
    
    
objects = obj(220,400)
object_group = pygame.sprite.Group()
object_group.add(objects)


############################ CREATING PLAYER CLASS #######################################
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, length, width):
        super().__init__()
        
        
        
        
        self.width = width
        self.height = length
        self.vel = 3
        
        self.char = pygame.transform.scale(idle_1,(length,width))
        
        
       
        
        self.walkLeft = [pygame.transform.scale(l1,(length,width)), 
                        pygame.transform.scale(l2,(length,width)), 
                        pygame.transform.scale(l3,(length,width)), 
                        pygame.transform.scale(l4,(length,width))]
     
       
        self.walkright = [pygame.transform.scale(r1,(length,width)), 
                        pygame.transform.scale(r2,(length,width)), 
                        pygame.transform.scale(r3,(length,width)), 
                        pygame.transform.scale(r4,(length,width))]
        
        self.walkdown = [pygame.transform.scale(d1,(length,width)), 
                        pygame.transform.scale(d2,(length,width)), 
                        pygame.transform.scale(d3,(length,width)), 
                        pygame.transform.scale(d4,(length,width))]
        
        
        self.walkup = [pygame.transform.scale(u1,(length,width)), 
                        pygame.transform.scale(u2,(length,width)), 
                        pygame.transform.scale(u3,(length,width)), 
                        pygame.transform.scale(u4,(length,width))]
        
        
        
        #image = self.walkLeft[int(current_sprite)]
        
        self.new_surface = pygame.Surface((45,45))
        self.new_surface.fill((255,255,255))
        self.new_surface_rect = self.new_surface.get_rect()
        
        
        self.image = self.new_surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.direction = 0
        
      
    def update(self):
        global walkCount
        global x
        
        
        
        if walkCount + 1 >= 4:
            walkCount = 0   
            
        if left:  
            window_surface.blit(self.walkLeft[int(walkCount)], (self.rect.x,self.rect.y))
            walkCount += 0.2
            
        
        elif right:
            window_surface.blit(self.walkright[int(walkCount)], (self.rect.x,self.rect.y))
            walkCount += 0.2
            
            
        
        elif up:  
            window_surface.blit(self.walkup[int(walkCount)], (self.rect.x,self.rect.y))
            walkCount += 0.2
           
        
        elif down:  
            window_surface.blit(self.walkdown[int(walkCount)], (self.rect.x,self.rect.y))
            walkCount += 0.2
            
                 
        else:
            window_surface.blit(self.char, (self.rect.x, self.rect.y))
            walkCount = 0
            
        #window_surface.blit(self.new_surface, (self.rect.x, self.rect.y))
        pygame.display.update()
        
        
       
   
    def movement(self):
        global walkCount
        global x
        global y
        global left
        global right
        global up
        global down
        dx = 0
        dy = 0
        
            
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            dx -= 3
            left = True
            right = False
            up = False
            down = False
            self.counter += 1
            self.direction = -1
            
        elif keys[pygame.K_d]:
            dx += 3
            self.counter += 1
            self.direction = 1
            left = False
            right = True
            up = False
            down = False
            
        elif keys[pygame.K_w]:
            dy -= 3
            self.counter += 1
            self.direction = -1
            up = True
            left = False
            right = False
            down = False
        elif keys[pygame.K_s]:
            dy += 3
            self.counter += 1
            self.direction = 1  
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
        
            
            
            
            
            
        #def player_rect():
        #    collide_dx =
        #    collide_dy = 
            
        #check for collision
        
        
        for tile in world.tile_list:
            
            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0 
       
            
        for obj in world.obj_list:
            if obj[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
                print("collided with tree!!!")
                merchant()
            if obj[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                print("collided with tree!!!")
                #merchant()
                
        for interact in world.interact_list:
            if interact[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0
                #stats["experience_points"] += 5
                #print(stats["experience_points"])
            if interact[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                #stats["experience_points"] += 5
                #print(stats["experience_points"])
                #merchant()
            #check for collision in y direction
            #if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground i.e. jumping
            #    if self.vel < 0:
             #       dy = tile[1].bottom - self.rect.top
              #      self.vel = 0
                #check if above the ground i.e. falling
               # elif self.vel >= 0:
                #    dy = tile[1].top - self.rect.bottom
                 #   self.vel = 0
                
            
        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
        elif self.rect.top > screen_height:
            self.rect.top = screen_height
            dy = 0
        #draw player onto screen
        #window_surface.blit(self.image, self.rect)
    
    #def collision(self):
    #    if obj1.mask.overlap(obj2.mask, offset(obj1, obj2)):
    #        print("collision!!!")
        
        
        
        
        
        #pos = pygame.mouse.get_pos()
        #if self.rect.colliderect(test_object_rect):
        #    for i in range(1,6):
        #        print("hit", i)
        #pygame.draw.rect(window_surface, (255,255,255), self.rect, 1)
        #if self.player_hitboxrect.colliderect(test_object_rect):
        #    print('collision')    
        
def exp_gained():
    if stats["curr_exp"] >= stats["exp_points_limit"]:
        level_up_sound.play()
        stats["exp_level"] += 1
        if stats["exp_level"] >= 1 and stats["exp_level"] <= 9:
            stats["exp_points_limit"] += 150
            stats["curr_exp"] = 0
            stats["health"] += 1
            
    if stats["curr_exp"] >= stats["exp_points_limit"]:
        
        stats["exp_level"] += 1
        if stats["exp_level"] >= 9 and stats["exp_level"] <= 19:
            stats["exp_points_limit"] += 500
            stats["curr_exp"] = 0
            stats["health"] += 1
    if stats["curr_exp"] >= stats["exp_points_limit"]:
        
        stats["exp_level"] += 1
        if stats["exp_level"] >= 19 and stats["exp_level"] <= 29:
            stats["exp_points_limit"] += 1000
            stats["curr_exp"] = 0
            stats["health"] += 1
    if stats["curr_exp"] >= stats["exp_points_limit"]:
        
        stats["exp_level"] += 1
        if stats["exp_level"] >= 29 and stats["exp_level"] <= 39:
            stats["exp_points_limit"] += 1500
            stats["curr_exp"] = 0
            stats["health"] += 1
            
    return True    



player = Player(80,80, 45, 45)   
player_group = pygame.sprite.Group()
player_group.add(player)

sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')
tile_size = 32

def achievement_points():
    pass

class World():
    def __init__(self, data):
        self.tile_list = []
        self.obj_list = []
        self.interact_list = []
        #load images
        test_object = pygame.image.load(os.path.join(sprites_dir,"objects","ramenshop_tile.png"))

        dirt_img = pygame.image.load(os.path.join(sprites_dir, "objects", "rock_tile.png"))
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == "H":
                    img = pygame.transform.scale(test_object, (128, 128))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.obj_list.append(tile)
                    
                if tile == "T":
                    img = pygame.transform.scale(test_object, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.interact_list.append(tile)
                if tile == "E":
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            window_surface.blit(tile[0], tile[1])
        for obj in self.obj_list:
            window_surface.blit(obj[0], obj[1])
            #pygame.draw.rect(window_surface, (255, 255, 255), tile[1], 2)
            
    
############################ CREATING BUTTON CLASS #######################################
class Button():
    def __init__(self,x, y, default_image, hovering_image, current_image):
        #self.image = image
        self.current_image = current_image
        self.default_image = default_image
        self.hovering_image = hovering_image
        
        self.rect = self.current_image.get_rect(topleft = (screen_width*x, screen_height*y))
        self.click = False
        
        self.button_hover = False
        
    def update(self):
        pos = pygame.mouse.get_pos()
        action = False
        window_surface.blit(self.current_image, self.rect)
        
        if self.rect.collidepoint(pos):
            self.current_image = self.hovering_image
            
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
            self.current_image = self.default_image
            self.button_hover = False
        return action

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, "H", 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, "E", 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, "T", 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]        
world = World(world_data)

def Merchant_Window():
    running = True
    while running:
        menu_surface = pygame.image.load(os.path.join(sprites_dir, "panal", "menu_ui_1.png"))
        merchant_window = pygame.transform.scale(menu_surface, (500,550/2))
        merchant_window_rect = merchant_window.get_rect(center = (screen_width/2, screen_height*.9))
        window_surface.blit(merchant_window, merchant_window_rect)

        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

enter_button = Button(.15, .72, new_default_tab, new_hovering_tab, new_default_tab)      
exit_button = Button(.34, .72, new_default_tab, new_hovering_tab, new_default_tab)  

def merchant():
    bubble_pop_sound.play()
    running = True
    
    question_text = algard_font.render("Would you like to enter?", False, (0,0,0))
    question_text_rect = question_text.get_rect(center = (295, screen_height*.8))

    
    enter_text = algard_font.render("Yes", False, ((0,0,0)))
    enter_text_rect = enter_text.get_rect(center = (200, screen_height*.9))
    

    no_text = algard_font.render("No", False, ((0,0,0)))
    no_text_rect = no_text.get_rect(center = (300, screen_height*.9))
    while running:
        menu_surface = pygame.image.load(os.path.join(sprites_dir, "panal", "menu_ui_1.png"))
        merchant_window = pygame.transform.scale(menu_surface, (500,550/2))
        merchant_window_rect = merchant_window.get_rect(center = (screen_width/2, screen_height*.9))
        window_surface.blit(merchant_window, merchant_window_rect)
        
        if enter_button.update():
            Merchant_Window()

        if exit_button.update():
            running = False
        
        window_surface.blit(question_text, question_text_rect)
        window_surface.blit(no_text, no_text_rect)
        window_surface.blit(enter_text, enter_text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
################################# CREATING EXIT MENU #######################################

                    
                    
                    
                    
menu_button1 = Button(.24, .72, new_default_tab, new_hovering_tab, new_default_tab)
menu_button2 = Button(.38, .72, new_default_tab, new_hovering_tab, new_default_tab)                    
menu_button3 = Button(.51, .72, new_default_tab, new_hovering_tab, new_default_tab)                    
menu_button4 = Button(.64, .72, new_default_tab, new_hovering_tab, new_default_tab)                 
################################# CREATING PAUSE MENU #######################################

def get_rect(text_name, loc_x, loc_y):
    text_loc_rect = text_name.get_rect()
    text_loc_rect.topleft = (screen_width*loc_x, screen_height*loc_y)
    return text_loc_rect

        
        
        
def Status_menu():
    
    # can improve menu system by making it a class object
    # make it liek the button system so the only thing it can change is the main menu screen 
    # in the middle
    # since right now the only way to change the main menu screen is to call a different
    # function screen where i have to repeat making the buttons and everything else
    run = True
    
    #menu_button = pygame.transform.scale(new_default_button, (300, 100))
    
    
    
    
    
    stats_text = font.render("Status", True, (200,150,50))
    stats_text_get_rect = get_rect(stats_text, .43, 0.15)
    
    
    
    
    exp_text = font.render(str("exp:")+str(stats["curr_exp"]), True, (200,150,50))
    exp_text_get_rect = get_rect(exp_text, .6, 0.28)
    
    level_text = font.render(str("Lv:")+str(stats["exp_level"]), True, (200,150,50))
    level_text_get_rect = get_rect(level_text, .6, 0.25)
    
    
    name_text = font.render(str("NAME:")+str("???"), True, (200,150,50))
    name_text_get_rect = get_rect(name_text, .28, 0.25)
    
    job_text = font.render(str("JOB:")+str("???"), True, (200,150,50))
    job_text_get_rect = get_rect(job_text, .28, 0.28)
    
    title_text = font.render(str("TITLE:")+str("???"), True, (200,150,50))
    title_text_get_rect = get_rect(title_text, .28, 0.31)
    
    fatigue_text = font.render(str("FATIGUE:")+str(), True, (200,150,50))
    fatigue_text_get_rect = get_rect(fatigue_text, .28, 0.45)
    
    # NOT UPDATING REAL TIME // FIX LATER
    health_text = font.render(str("HP:")+str(stats["health"]), True, (200,150,50))
    health_text_get_rect = get_rect(health_text, .28, 0.40)
    # NOT UPDATING REAL TIME // FIX LATER
    mana_text = font.render(str("MP:")+str(stats["mana"]), True, (200,150,50))
    mana_text_get_rect = get_rect(mana_text, .6, 0.4)
    # NOT UPDATING REAL TIME // FIX LATER
    strength_text = font.render(str("STRENGTH:")+str(stats["stamina"]), True, (200,150,50))
    strength_text_get_rect = get_rect(strength_text, .28, 0.57)
    
    

    hovering_tab_img = get_rect(new_hovering_tab_get_rect, .24, .72)
    
    

    while run:
        #background_surface()
        
        ########################## idk what this is ############################################

        new_tab = pygame.Surface((400, 600), 0, window_surface)
        new_tab.fill((200,150,50))
        
        new_tab_rect = new_tab.get_rect()
        new_tab_rect.center = (screen_width*.50, screen_height*.4)
        
        ########################## main stat screen ############################################
        
        
        scaling_menu_surface = pygame.image.load(os.path.join(sprites_dir, "panal", "Stats_ui_3_0.png"))
        menu_surface = pygame.transform.scale(scaling_menu_surface, (400,600))
        
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (screen_width*.50, screen_height*.4)
        
        ########################### drawing #########################################
        window_surface.blit(menu_surface, menu_rect)
        window_surface.blit(stats_text, (stats_text_get_rect))
        
        
        ############################ buttons #########################################
        
        
        window_surface.blit(new_hovering_tab_get_rect, (hovering_tab_img))
            
        
        if menu_button2.update():
            Quest_menu()
        
        
        if menu_button3.update():
            exp_gained()
            stats["mana"] += 1
            stats["curr_exp"] += 50
        
        
        if menu_button4.update():
            Exit_menu()
            
            
        window_surface.blit(font.render(str("exp:")+str(stats["curr_exp"]), True, (200,150,50)), exp_text_get_rect)
        window_surface.blit(font.render(str("Lv:")+str(stats["exp_level"]), True, (200,150,50)), level_text_get_rect)
        window_surface.blit(name_text, (name_text_get_rect))
        window_surface.blit(job_text, (job_text_get_rect))
        window_surface.blit(title_text, (title_text_get_rect))
        window_surface.blit(fatigue_text, (fatigue_text_get_rect))
        window_surface.blit(health_text, (health_text_get_rect))
        window_surface.blit(mana_text, (mana_text_get_rect))
        window_surface.blit(strength_text, (strength_text_get_rect))
        
        pygame.display.update()
        clock.tick(120)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write_save(stats)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_pop_up_sound.play()
                    game_sound.play(-1)
                    state_stack[game_scene()]

# // create openable quests //




def Quest_menu():
    run = True
    
    
    
    
    
    stats_text = font.render("Quests", True, ((200,150,50)))
    stats_text_get_rect = get_rect(stats_text, .43, 0.15)
    
    
    hovering_tab_img2 = get_rect(new_hovering_tab_get_rect2, .38, .72)
    
    quest_text = font.render(str("QUEST NAME:")+str("???"), True, (200,150,50))
    quest_text_get_rect = get_rect(quest_text, .28, 0.25)
    
    details_text = font.render(str("DETAILS:")+str("???"), True, (200,150,50))
    details_text_get_rect = get_rect(details_text, .28, 0.28)
    
    reward_text = font.render(str("REWARD:")+str("???"), True, (200,150,50))
    reward_text_get_rect = get_rect(reward_text, .28, 0.31)
    
    
    
    while run:
        #background_surface()
        ##################################################################################
        scaling_menu_surface = pygame.image.load(os.path.join(sprites_dir, "panal", "Stats_ui_3_0.png"))
        menu_surface = pygame.transform.scale(scaling_menu_surface, (400,600))
       
        
        
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (screen_width*.50, screen_height*.4)
        
        
        window_surface.blit(menu_surface, menu_rect)
        window_surface.blit(stats_text, (stats_text_get_rect))
        scroll_method.Render()
        
        
        
        
        
        
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                write_save(stats)
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_sound.play(-1)
                    state_stack[game_scene()]
            
            
        
        
        if menu_button1.update():
            Status_menu()
        
            
        window_surface.blit(new_hovering_tab_get_rect2, (hovering_tab_img2))
            
        if menu_button3.update():
            exp_gained()
            stats["mana"] += 1
            stats["curr_exp"] += 50
            
        if menu_button4.update():
            Exit_menu()
        
        #window_surface.blit(quest_text, (quest_text_get_rect))
        #window_surface.blit(details_text, (details_text_get_rect))
        #window_surface.blit(reward_text, (reward_text_get_rect))
        
        
        
        
        
        pygame.display.update()
        
        
def Exit_menu():
    run = True
    
    
    
    
    exit_button = Button(.55, .25, new_default_button, new_hovering_button, new_default_button)
    stats_text = font.render("Settings:", True, ((200,150,50)))
    stats_text_get_rect = get_rect(stats_text, .43, 0.15)
    
    
    
    
    quest_text = font.render(str("Home:")+str("???"), True, (200,150,50))
    quest_text_get_rect = get_rect(quest_text, .28, 0.25)
    
    details_text = font.render(str("Settings:")+str("???"), True, (200,150,50))
    details_text_get_rect = get_rect(details_text, .28, 0.28)
    
    reward_text = font.render(str("Exit:")+str("???"), True, (200,150,50))
    reward_text_get_rect = get_rect(reward_text, .28, 0.31)
    
    hovering_tab_img2 = get_rect(new_hovering_tab_get_rect, .64, .72)
    while run:
        #background_surface()
        ##################################################################################
        scaling_menu_surface = pygame.image.load(os.path.join(sprites_dir, "panal", "Stats_ui_3_0.png"))
        menu_surface = pygame.transform.scale(scaling_menu_surface, (400,600))
       
        
        
        menu_rect = menu_surface.get_rect()
        menu_rect.center = (screen_width*.50, screen_height*.4)
        
        
        window_surface.blit(menu_surface, menu_rect)
        window_surface.blit(stats_text, (stats_text_get_rect))
        
        
        
        if menu_button1.update():
            Status_menu()
        
        if menu_button2.update():
            Quest_menu()    
       
            
        if menu_button3.update():
            exp_gained()
            stats["mana"] += 1
            stats["curr_exp"] += 50
        
        if exit_button.update():
            state_stack[menu()]
        
        window_surface.blit(new_hovering_tab_get_rect2, (hovering_tab_img2))
            
        window_surface.blit(quest_text, (quest_text_get_rect))
        window_surface.blit(details_text, (details_text_get_rect))
        window_surface.blit(reward_text, (reward_text_get_rect))
      
        pygame.display.update()
        clock.tick(120)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write_save(stats)
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_sound.play(-1)
                    state_stack[game_scene()]
################################# DEFAULT FADING TRANISITION #######################################
def Transition_screen(width, height, current_scene):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(190, 300):
        fade.set_alpha(alpha)
        #cat_animation()
        enter_text = algard_font.render("Loading %", False, ((200,150,50)))
        
        
        
        window_surface.blit(current_scene, (0,0))
        
        window_surface.blit(fade, (0,0))
        window_surface.blit(enter_text, (25,850))
        pygame.display.update()
        pygame.time.delay(5)
           
################################ ======================= ###################################
def background_surface():
    #fade = pygame.Surface((width, height))
    #fade.fill((200,170,100))
    
        
    window_surface.blit(game_map, (0,0))
    
        
       


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
    game_text = title_algard_font.render("Task RPG", False, ((255,255,255)))
    game_text_rect = get_rect(game_text, 0.25,0.17)
    
    game_text2 = font.render(" @anjiblob", False, ((0,0,0)))
    game_text_rect2 = get_rect(game_text2, 0.65,.97)
    
    #music_sound.pause()
    
    running = True
    button_1 = Button(.05, .65, new_default_button, new_hovering_button, new_default_button)
    button_2 = Button(.05, .75, new_default_button, new_hovering_button, new_default_button)
    button_3 = Button(.05, .85, new_default_button, new_hovering_button, new_default_button)
    
    
    menu_background = pygame.image.load(os.path.join(background_dir, "lofi_image.jpg"))
    
    while running:
         
         window_surface.blit(menu_background, (-820,-200))
         
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
             
         window_surface.blit(game_text, (game_text_rect))
         
         window_surface.blit(game_text2, (game_text_rect2))
         
         pygame.display.flip()
         clock.tick(120)
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
        
        

################################# OPTIONS SCREEN / LOAD SCREEN TEMP #######################################
def load_scene():
    global window_surface
    
    running = True
    options_button_1 = Button(250, 150, new_default_button, new_hovering_button, new_default_button)
    options_button_2 = Button(370, 150, new_default_button, new_hovering_button, new_default_button)
    options_button_3 = Button(370, 250, new_default_button, new_hovering_button, new_default_button)
    
    load_game_background = pygame.image.load(os.path.join(background_dir, "town.png"))
    #load_game_background = pygame.transform.scale(scaling_load_game_background, (500,800))
    while running:
        window_surface.blit(load_game_background, (0,0))
        
        
        if options_button_1.update():
            options["sound"] -= 0.1
            
        if options_button_2.update():
            options["sound"] += 0.1
        
        if options_button_3.update():
            pygame.display.set_mode((1280, 720))
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    window_surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                
        
        
        window_surface.blit(font.render(str("Sound Level:")+str(options["sound"]), True, (255, 255, 255)), (32, 48))
            
        pygame.display.update()
        clock.tick(120)
        
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
    game_sound.play(-1)
    
    running = True
    
    while running:
        
        window_surface.blit(game_map, (0,0))
        #window_surface.blit(test_object, test_object_rect)
        #pygame.draw.rect(window_surface, (0,0,0), obstacle, 4)
        
        
        
        #object_group.draw(window_surface)
        window_surface.blit(game_background, (0, 0))
        

        world.draw()
        player.update()
        player.movement()
        
        
        
        pygame.display.flip()
        
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write_save(stats)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #Transition_screen(screen_width, screen_height, game_background)
                    #state_stack[menu()]
                    write_save(stats)
                    
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_pop_up_sound.play()
                    game_sound.fadeout(300)
                    Status_menu()
        
        
        
scroll_method = Scroll(window_surface, screen_width, screen_height, state_stack, game_scene, stats)       
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
        mins = sec // 60 # minutes left
        day = (counter // 86400) 
        if hour >= 24 and mins >= 0:
            hour = hour - (24*day)
        sec %= 60
        
        
        
     
            
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter -= 1
                
                if counter > 0:
                    #text = str(counter).rjust(3)
                    text = ("Time remaining: "+str(day)+":"+str(hour)+":"+str(mins)+":"+str(sec))
                    if sec < 10:
                        text = ("Time remaining: "+str(day)+":"+str(hour)+":"+str(mins)+":"+"0"+str(sec))
                        if sec < 10 and mins < 10:
                            text = ("Time remaining: "+str(day)+":"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                            if sec < 10 and mins < 10 and hour < 10:
                                text = ("Time remaining: "+str(day)+":"+"0"+":"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                                if sec < 10 and mins < 10 and hour < 10 and day < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+":"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                    if mins < 10:
                        text = ("Time remaining: "+str(day)+":"+str(hour)+":"+"0"+str(mins)+":"+str(sec))
                        if mins < 10 and sec < 10:
                            text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                            if mins < 10 and hour < 10 and sec < 10:
                                text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                                if mins < 10 and hour < 10 and sec < 10 and day < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                                
                            
                    if hour < 10:
                        text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+str(mins)+":"+str(sec))
                        if hour < 10 and mins < 10:
                            text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+str(sec))
                            if hour < 10 and mins < 10 and sec < 10:
                                text = ("Time remaining: "+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                                if hour < 10 and day < 10 and mins < 10 and sec < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
                    if day < 10:
                        text = ("Time remaining: "+"0"+str(day)+":"+str(hour)+":"+str(mins)+":"+str(sec))
                        if day < 10 and hour < 10:
                            text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+str(mins)+":"+str(sec))
                            if day < 10 and hour < 10 and mins < 10:
                                text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+str(sec))
                                if day < 10 and hour < 10 and mins < 10 and sec < 10:
                                    text = ("Time remaining: "+"0"+str(day)+":"+"0"+str(hour)+":"+"0"+str(mins)+":"+"0"+str(sec))
    
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
        clock.tick(120)
        
        
        


  
        
################################# CALLING MENU SCREEN #######################################
if __name__ == "__main__":
    #StartUp_screen()
    menu()
    
    
    
    