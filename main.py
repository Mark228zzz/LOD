import pygame
from draw import Draw
from game import Game
from vars import *
from creatures.animal import Animal
from structures.obstacle import Obstacle

def main():
    pygame.init()
    Game.init_game()

    animal = Animal(9, 7, (0, 0, 0))
    obstacle = Obstacle(10, 7, (255, 255, 50))

    while Game.run:
        pygame.time.delay(150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
                break

        Game.window.fill((255, 255, 255))

        Draw.grid()
        Draw.all()

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
