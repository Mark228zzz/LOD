from windows.window import Window
import pygame
from vars import List


class DebugWindow(Window):
    def draw(self):
        if not self.visible: return
        font = pygame.font.SysFont('arial', 14)
        info_animal   = font.render(f'Animals  : {len(List.animals)}', True, (0, 0, 0), (200, 200, 200))
        info_food     = font.render(f'Foods    : {len(List.foods)}', True, (0, 0, 0), (200, 200, 200))
        info_predator = font.render(f'Predators: {len(List.predators)}', True, (0, 0, 0), (200, 200, 200))
        self.game_window.blit(info_animal, (5, 14))
        self.game_window.blit(info_food, (5, 28))
        self.game_window.blit(info_predator, (5, 42))
