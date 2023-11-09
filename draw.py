import pygame
from game import Game
from vars import *


class Draw:
    @staticmethod
    def all():
        Draw.debug_window()

        for animal in List.animals: # draw all animals that are alive
            pygame.draw.rect(Game.window, animal.color, (animal.x, animal.y, animal.width, animal.height))
        for food in List.foods: # draw all foods that wasn`t eatten
            pygame.draw.rect(Game.window, food.color, (food.x, food.y, food.width, food.height))
        for predator in List.predators: # draw all predators that are alive
            pygame.draw.rect(Game.window, predator.color, (predator.x, predator.y, predator.width, predator.height))

    @staticmethod
    def debug_window():
        font = pygame.font.SysFont('arial', 10)
        info_animal = font.render(f'Animals: {len(List.animals)}', True, (0, 0, 0), (200, 200, 200))
        info_food = font.render(f'Foods: {len(List.foods)}', True, (0, 0, 0), (200, 200, 200))
        Game.window.blit(info_animal, (5, 5))
        Game.window.blit(info_food, (5, 15))
