import pygame
from game import *
from creature import *
from windows.debug_window import *
from obstacle import Obstacle

pygame.init()

Game.init_game()
debug_window = DebugWindow()

while Game.run:
    pygame.time.delay(150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.run = False
            break
        elif event.type == pygame.VIDEORESIZE:
            Game.window_width, Game.window_height = event.w, event.h
            Game.window = pygame.display.set_mode((Game.window_width, Game.window_height), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SLASH:
                Game.debug_window = not Game.debug_window
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Game.add_smth_at_click(event.pos, Food)
            elif event.button == 2:
                Game.add_smth_at_click(event.pos, Obstacle)
            elif event.button == 3:
                Game.add_smth_at_click(event.pos, Creature)

    Game.window.fill((255, 255, 255))
    Game.draw_biomes()
    Game.loop()
    Game.draw_grid()
    Game.draw_obstacles()
    Game.draw_creatures()
    Game.draw_foods()

    if Game.debug_window: debug_window.draw()

    pygame.display.update()

pygame.quit()
