import pygame
from game import *


class DebugWindow:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.window = pygame.Surface((Game.window_width, Game.window_height))
        self.window.set_alpha(150)
        self.window.fill((20, 20, 20))

    def draw(self):
        font = pygame.font.Font(None, 25)
        y = 45
        pygame.draw.rect(Game.window, (200, 200, 200), (40, 40, 200, 200))
        debug_text = [
            f"Creatures: {len(Game.list_of_creatures)}",
            f"Foods: {len(Game.list_of_foods)}",
            f"Obstacles: {len(Game.list_of_obstacles)}"
        ]
        for line in debug_text:
            text_surface = font.render(line, True, (255, 0, 255))
            Game.window.blit(text_surface, (60, y))
            y += 40
