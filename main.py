import pygame
from draw import Draw
from game import Game
from vars import *
from creatures.animal import Animal
from random import randint
from foods.food import Food

def spawn_food():
    if randint(0, 12) == 0:
        food = Food(randint(0, Const.WIDTH), randint(0, Const.HEIGHT), 10, 10, (255, 0, 255))

def main():
    pygame.init()
    Game.init_game()

    animal = Animal(300, 300, 10, 10, (255, 0, 0))

    while Game.run:
        pygame.time.delay(1)
        print(len(List.animals))

        for animal in List.animals:
            animal.loop()

        for predator in List.predators:
            predator.loop()

        Game.window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
                break

        spawn_food()
        Draw.all()

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
