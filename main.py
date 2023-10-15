import pygame
from game import *
from creature import *
from windows.debug_window import *

pygame.init()

life = Creature()
Game.init_game()
debug_window = DebugWindow()

while Game.run:
    pygame.time.delay(75)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.run = False
            break
        elif event.type == pygame.VIDEORESIZE:
            Game.window_width, Game.window_height = event.w, event.h
            Game.window = pygame.display.set_mode((Game.window_width, Game.window_height), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Game.add_food_at_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_w:
                debug_window.toggle_visibility()
    
    Game.window.fill((255, 255, 255))
    Game.loop()
    Game.draw_obstacles()
    Game.draw_grid()
    Game.draw_creatures()
    Game.draw_foods()
    debug_window.draw(Game.window)
    pygame.display.update()

pygame.quit()
