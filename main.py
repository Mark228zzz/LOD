import pygame
from draw import Draw
from game import Game
from vars import *
from creatures.animal import Animal
from structures.obstacle import Obstacle

def main():
    pygame.init()
    Game.init_game()

    animal = Animal(9, 7, 10, 10, (255, 0, 0))

    while Game.run:
        pygame.time.delay(5)
        animal.loop()
        Game.window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
                break

        Draw.all()

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
