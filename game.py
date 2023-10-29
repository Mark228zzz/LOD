import pygame
from vars import *


class Game:
    run = True
    window = None

    @staticmethod
    def init_game():
        Game.window = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("WINDOW")
