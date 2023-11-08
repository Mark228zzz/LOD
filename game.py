import pygame
from vars import *
from creatures.animal import Animal
from creatures.predator import Predator

class Game:
    run = True
    window = None

    @staticmethod
    def init_game():
        Game.window = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("WINDOW")

        animal = Animal(300, 300, 10, 10, (255, 0, 0))
        predator = Predator(240, 100, 15, 15, (0, 0, 0))

    @staticmethod
    def loops():
        for animal in List.animals:
            animal.loop()

        for predator in List.predators:
            predator.loop()
