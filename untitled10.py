# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:33:41 2022

@author: Noatok
"""
import pygame, sys, os





############################ FUTURE PATCHES #############################################

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
algard_font = pygame.font.Font("alagard.ttf", 40)




############################ DATA / LISTS #######################################



############################ SAVE/LOAD SYSTEM #######################################


 

############################ IMAGES #######################################


game_background = pygame.image.load(os.path.join(map_dir, "grass.png"))
game_map = pygame.transform.scale(game_background, (1100, screen_height))


test_object = pygame.image.load(os.path.join(map_dir, "tree.png"))
test_object_rect = test_object.get_rect()
print(test_object_rect)
#test_object_rect.center = (300,400)
#test_object = pygame.Surface((128,128))
#test_object.fill((200,150,50))
#test_object_rect = test_object.get_rect()
#test_object_rect.center = (300,400)

obstacle = pygame.Rect(400,200, 80,80)


menu_background = pygame.image.load(os.path.join(background_dir, "wallpaper5.jpg"))



############################ BUTTONS ######################################


# RECTANGLE BUTTONS
default_button = pygame.image.load(os.path.join(sprites_dir, "button", "button2.0.png"))
new_default_button = pygame.transform.scale(default_button, (100,80))

hovering_button = pygame.image.load(os.path.join(sprites_dir, "button", "buttonpress2.0.png"))
new_hovering_button = pygame.transform.scale(hovering_button, (100,100))


# MENU TABS
default_tab = pygame.image.load(os.path.join(sprites_dir, "button", "tab_unselected.png"))
new_default_tab = pygame.transform.scale(default_tab, (100,80))

hovering_tab = pygame.image.load(os.path.join(sprites_dir, "button", "tab_selected.png"))
new_hovering_tab = pygame.transform.scale(hovering_tab, (100,100))











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


vel = 3


left = False
right = False
up = False
down = False
walkCount = 0




############################ CREATING PLAYER CLASS #######################################
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, length, width):
        super().__init__()
        
        
        
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        
        
        self.char = pygame.transform.scale(idle_1,(length,width))
        self.rect = self.char.get_rect()
        
       
    
        self.new_surface = pygame.Surface((45,45))
        self.new_surface.fill((255,255,255))
        self.new_surface_rect = self.new_surface.get_rect()
        
        
        
    
        pygame.sprite.spritecollide(Player, object_group, True)
            
        
        
        
    def update(self):
        global walkCount
        global x
        
        
        
        
        if walkCount + 1 >= 4:
            walkCount = 0   
            
        if left:  
            window_surface.blit(self.char, (self.x,self.y))
            walkCount += 0.2
            
        
        elif right:
            window_surface.blit(self.char, (self.x,self.y))
            walkCount += 0.2
            
            
        
        elif up:  
            window_surface.blit(self.char, (self.x,self.y))
            walkCount += 0.2
           
        
        elif down:  
            window_surface.blit(self.char, (self.x,self.y))
            walkCount += 0.2
            
                 
        else:
            window_surface.blit(self.char, (self.x, self.y))
            walkCount = 0
            
        #window_surface.blit(self.new_surface, (self.x, self.y))
        pygame.display.update()
        
        
            
            
            
    def movement(self):
        global walkCount
        global x
        global y
        global left
        global right
        global up
        global down
        global vel
        
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > vel: 
            self.x -= vel
            left = True
            right = False
            up = False
            down = False
            
        elif keys[pygame.K_d] and self.x < screen_width - vel - self.width:
            self.x += vel
            left = False
            right = True
            up = False
            down = False
            
            
        elif keys[pygame.K_w] and self.y > vel: 
            self.y -= vel
            up = True
            left = False
            right = False
            down = False
        elif keys[pygame.K_s] and self.y < screen_height - vel - self.width: 
            self.y += vel
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
            
    
    
   
        
        
player = Player(20,20, 45, 45)   
player_group = pygame.sprite.Group()
player_group.add(player)

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
def game_scene():
    
    
    running = True
    
    while running:
        
        window_surface.blit(game_map, (0,0))
        window_surface.blit(test_object, test_object_rect)
        pygame.draw.rect(window_surface, (0,0,0), obstacle, 4)
        
            
        object_group.draw(window_surface)
        
        player.movement()
        player.update()
        
        
        

       
        
        
        pygame.display.update()
        
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                pygame.quit()
                sys.exit()
            
                    
                    
if __name__ == "__main__":
    game_scene()