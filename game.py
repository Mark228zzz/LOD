import pygame
from food import *

class Game:
    run = True
    window_width, window_height = 800, 600
    grid_size = 20
    cols = window_width // grid_size
    rows = window_height // grid_size
    window = None
    list_of_creatures, list_of_foods, list_of_obstacles = [], [], []
    debug_window = False

    @staticmethod
    def init_game():
        grid = [['' for _ in range(Game.cols)] for _ in range(Game.rows)]
        Game.window = pygame.display.set_mode((Game.window_width, Game.window_height), pygame.RESIZABLE)

    @staticmethod
    def is_obstacle(x, y):
        return any(obstacle.x <= x < obstacle.x + obstacle.width and obstacle.y <= y < obstacle.y + obstacle.height for obstacle in Game.list_of_obstacles)

    @staticmethod
    def draw_grid():
        Game.cols = Game.window_width // Game.grid_size
        Game.rows = Game.window_height // Game.grid_size
        for y in range(Game.rows):
            for x in range(Game.cols):
                pygame.draw.rect(Game.window, (200, 200, 200), (x * Game.grid_size, y * Game.grid_size, Game.grid_size, Game.grid_size), 1)

    @staticmethod
    def draw_creatures():
        for creature in Game.list_of_creatures:
            pygame.draw.rect(Game.window, creature.color, (creature.x * Game.grid_size, creature.y * Game.grid_size, Game.grid_size, Game.grid_size))    

    @staticmethod
    def draw_foods():
        for food in Game.list_of_foods:
            pygame.draw.rect(Game.window, food.color, (food.x * Game.grid_size, food.y * Game.grid_size, Game.grid_size, Game.grid_size))

    @staticmethod
    def draw_obstacles():
        for obstacle in Game.list_of_obstacles:
            pygame.draw.rect(Game.window, obstacle.color, (obstacle.x * Game.grid_size, obstacle.y * Game.grid_size, obstacle.width * Game.grid_size, obstacle.height * Game.grid_size))

    @staticmethod
    def check(x, y):
        grid_x, grid_y = x // Game.grid_size, y // Game.grid_size

        if any(creature.x == grid_x and creature.y == grid_y for creature in Game.list_of_creatures):
            return False

        if any(food.x == grid_x and food.y == grid_y for food in Game.list_of_foods):
            return False

        if any(obstacle.x <= grid_x < obstacle.x + obstacle.width and obstacle.y <= grid_y < obstacle.y + obstacle.height for obstacle in Game.list_of_obstacles):
            return False

        return True


    @staticmethod
    def add_smth_at_click(pos, thing):
        grid_x, grid_y = pos[0] // Game.grid_size, pos[1] // Game.grid_size

        if any(creature.x == grid_x and creature.y == grid_y for creature in Game.list_of_creatures):
            return False

        if any(food.x == grid_x and food.y == grid_y for food in Game.list_of_foods):
            return False

        if any(obstacle.x <= grid_x < obstacle.x + obstacle.width and obstacle.y <= grid_y < obstacle.y + obstacle.height for obstacle in Game.list_of_obstacles):
            return False

        something = thing(x=grid_x, y=grid_y)

    @staticmethod
    def loop():
        for creature in Game.list_of_creatures:
            creature.decrease_hunger()
            creature.move_to_food()
            creature.reproduction()
