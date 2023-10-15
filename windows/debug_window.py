import pygame
from game import *

class DebugWindow:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.window = pygame.Surface((Game.window_width, Game.window_height))
        self.window.set_alpha(150)
        self.window.fill((20, 20, 20))
        self.visible = False
        
    def toggle_visibility(self):
        self.visible = not self.visible
        
    def draw(self, window):
        if self.visible:
            self.window.fill((20, 20, 20))
            info_text = [
                f'Count of creatures: {len(Game.list_of_creatures)}',
                f'Count of foods: {len(Game.list_of_foods)}',
                f'Count of obstacles: {len(Game.list_of_obstacles)}'
            ]
            y_offset = 10
            for line in info_text:
                text = self.font.render(line, True, (255, 255, 255))
                self.window.blit(text, (10, y_offset))
                y_offset += 40
            self.window.blit(self.window, (0, 0))
        