import pygame
from game import *
from creature import *

pygame.init()

life = Creature()
Game.init_game()

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
    
    Game.window.fill((255, 255, 255))
    Game.loop()
    Game.draw_obstacles()
    Game.draw_grid()
    Game.draw_creatures()
    Game.draw_foods()
    pygame.display.update()

pygame.quit()
