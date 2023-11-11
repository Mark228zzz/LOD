import pygame
from game import Game
from vars import List


class Draw:
    @staticmethod
    def all():
        for animal in List.animals: # draw all animals that are alive
            pygame.draw.rect(Game.window, animal.color, (animal.x, animal.y, animal.width, animal.height))
        for food in List.foods: # draw all foods that wasn`t eatten
            pygame.draw.rect(Game.window, food.color, (food.x, food.y, food.width, food.height))
        for predator in List.predators: # draw all predators that are alive
            pygame.draw.rect(Game.window, predator.color, (predator.x, predator.y, predator.width, predator.height))
        for window in List.windows:
            window.draw()
        for button in List.buttons:
            button.draw()
