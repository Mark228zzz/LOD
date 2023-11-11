import pygame
from vars import List, Const
from creatures.animal import Animal
from creatures.predator import Predator
from foods.food import Food
from windows.debug_window import DebugWindow
from random import randint


class Game:
    run = True
    window = None

    @staticmethod
    def init_game():
        with open('logs.txt', 'w') as logs: # reload logs
            logs.write('')

        Game.window = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        pygame.display.set_caption("LOD GAME")

        animal = Animal(randint(1, Const.WIDTH), randint(1, Const.HEIGHT), 10, 10, (255, 0, 0))
        predator = Predator(randint(1, Const.WIDTH), randint(1, Const.HEIGHT), 15, 15, (0, 0, 0))

        window = DebugWindow(Game.window, True) # create debug window

    @staticmethod
    def loops():
        for animal in List.animals:
            animal.loop()

        for predator in List.predators:
            predator.loop()

    @staticmethod
    def spawn_food():
        if randint(0, 12) == 0:
            _ = Food(randint(0, Const.WIDTH), randint(0, Const.HEIGHT), 10, 10, (255, 0, 255))
