import pygame
from vars import List, Const
from creatures.animal import Animal
from creatures.predator import Predator
from foods.food import Food
from windows.debug_window import DebugWindow
from buttons.button import Button
from random import randint


class Game:
    run = True
    window = None

    @staticmethod
    def init_game():
        with open('logs.txt', 'w') as logs: # reload logs
            logs.write('')

        # make window
        Game.window = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        pygame.display.set_caption("LOD GAME")

        # add objects in the start game
        animal = Animal(randint(1, Const.WIDTH), randint(1, Const.HEIGHT), 10, 10, (255, 0, 0))
        predator = Predator(randint(1, Const.WIDTH), randint(1, Const.HEIGHT), 15, 15, (0, 0, 0))

        window = DebugWindow(Game.window, True) # create debug window

        button = Button(Game.window, 100, 2, 165, 30, (0, 150, 0), (0, 180, 0), (255, 255, 255), "ENABLE DEBUG WINDOW")

    @staticmethod
    def loops(): # do loops for all objects in the game
        for animal in List.animals:
            animal.loop()

        for predator in List.predators:
            predator.loop()

        for button in List.buttons:
            button.loop()

    @staticmethod
    def spawn_food(): # random spawn food
        if randint(0, 12) == 0:
            _ = Food(randint(0, Const.WIDTH), randint(0, Const.HEIGHT), 10, 10, (255, 0, 255))
