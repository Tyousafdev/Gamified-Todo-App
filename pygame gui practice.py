import pygame
import pygame_gui
import sys,os


pygame.init()
window_width = 800
window_height = 600
window_surface = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()
fps = 60

assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")
sprites_dir = os.path.join(assets_dir, "sprites")
background2 = pygame.image.load(os.path.join(sprites_dir, "panal", "Stats_ui_3_0.png")) 
background2_rect = background2.get_rect()

assets_dir = os.path.join("assets")
sprites_dir = os.path.join(assets_dir, "sprites")
background_dir = os.path.join(assets_dir,"background")
sound_dir = os.path.join(assets_dir, "sounds")
map_dir = os.path.join(assets_dir, "map")
font_dir = os.path.join(assets_dir, "font")


font = pygame.font.SysFont('Consolas', 20)
#background surface
background = pygame.Surface((window_width,window_height))
background.fill((255,255,200))

game_background = pygame.Surface((window_width, window_height))
game_background.fill((255,200,200))


manager = pygame_gui.UIManager((window_width,window_height),'theme.json')

hello_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((100,200),(200,60)), text = "start", manager = manager)
exit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((100,300), (200,60)), text = "exit", manager = manager)

stats_text = font.render("Status", True, (200,150,50))
text_box = pygame_gui.elements.UITextBox(html_text = "d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4d0f78929d9c00f4a73d292aa0c0d2cb4", relative_rect = background2_rect, manager = manager, )

options = ("pick", "yes", "no", "maybe", "idk")
menu_box = pygame_gui.elements.UIDropDownMenu(options_list = options, starting_option = options[0], relative_rect = pygame.Rect((400,200),(100,60)), manager = manager)
print(menu_box.ui_theme)


def main():
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        window_surface.blit(background, (0,0))
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    game()
                
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    pygame.quit()    
                    sys.exit()
                    
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == menu_box:
                    print("yes")
                else:
                    print("other")
            manager.process_events(event)
            
        manager.update(time_delta)
        
        manager.draw_ui(window_surface)
        pygame.display.update()
        clock.tick(fps)

        
def game():
    running = True
    while running:
        window_surface.blit(game_background, (0,0))
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
if __name__ == "__main__":
    main()