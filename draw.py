import pygame
from game import Game
from vars import *


class Draw:
    @staticmethod
    def all():
        for animal in List.animals:
            pygame.draw.rect(Game.window, animal.color, (animal.x, animal.y, animal.width, animal.height))
        for food in List.foods:
            pygame.draw.rect(Game.window, food.color, (food.x, food.y, food.width, food.height))
        for predator in List.predators:
            pygame.draw.rect(Game.window, predator.color, (predator.x, predator.y, predator.width, predator.height))
