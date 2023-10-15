import pygame
import random

pygame.init()


class Game:
    run = True
    window_width, window_height = 800, 600
    grid_size = 30
    cols = window_width // grid_size
    rows = window_height // grid_size
    window = None
    list_of_creatures, list_of_foods, list_of_obstacles = [], [], []
    
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
    def loop():
        for creature in Game.list_of_creatures:
            creature.decrease_hunger()
            creature.move_to_food()
            creature.reproduction()


class Obstacle:
    def __init__(self, x: int, y: int, width: int = 1, height: int = 1, color: tuple = (150, 75, 0)):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        
        Game.list_of_obstacles.append(self)


class Creature:
    def __init__(self, x: int = Game.cols // 2, y: int = Game.rows // 2, color: tuple = (0, 0, 255)):
        self.x = x
        self.y = y
        self.hunger = 150
        self.age = 0
        self.color = color
        self.search_radius = 50
        self.alive = True
        
        Game.list_of_creatures.append(self)
    
    def move_to_food(self):
        if self.alive:
            if self.hunger < 100:
                nearest_food = None
                nearest_distance = float('inf')

                for food in Game.list_of_foods:
                    distance = ((food.x - self.x)**2 + (food.y - self.y)**2)**0.5
                    if distance < self.search_radius and distance < nearest_distance:
                        nearest_food = food
                        nearest_distance = distance

                if nearest_food is not None:
                    new_x, new_y = self.x, self.y

                    if new_x < nearest_food.x and not Game.is_obstacle(self.x + 1, self.y):
                        new_x += 1
                    elif new_x > nearest_food.x and not Game.is_obstacle(self.x - 1, self.y):
                        new_x -= 1

                    if new_y < nearest_food.y and not Game.is_obstacle(self.x, self.y + 1):
                        new_y += 1
                    elif new_y > nearest_food.y and not Game.is_obstacle(self.x, self.y - 1):
                        new_y -= 1
                        
                    if not Game.is_obstacle(new_x, new_y):
                        self.x, self.y = new_x, new_y

                    if self.x == nearest_food.x and self.y == nearest_food.y:
                        self.hunger += nearest_food.satiety
                        Game.list_of_foods.remove(nearest_food)
                else:
                    self.random_move()
            else:
                self.random_move()
        else:
            Game.list_of_creatures.remove(self)
        
        if self.age >= random.randint(100, 150):
            Game.list_of_creatures.remove(self)
        else:
            self.age += 1
        
    def reproduction(self):
        if self.hunger >= 160:
            if random.randint(1, 15) == 1:
                self.hunger -= 65
                life = Creature(x=self.x, y=self.y, color=(self.color[0]+2, 0, 255))
    
    def random_move(self):
        random_direction = (random.choice(['x', 'y']), random.choice([-1, 1]))
        match random_direction[0]:
            case 'x':
                if 0 <= self.x + random_direction[1] < Game.window_width and not Game.is_obstacle(self.x + random_direction[1], self.y):
                    self.x += random_direction[1]
            case 'y':
                if 0 <= self.y + random_direction[1] < Game.window_height and not Game.is_obstacle(self.x, self.y + random_direction[1]):
                    self.y += random_direction[1]
    
    def decrease_hunger(self):
        if not self.hunger <= 0:
            self.hunger = max(0, self.hunger - 1)
        else:
            self.alive = False


class Food:
    def __init__(self, x: int, y: int, satiety: int = 100):
        self.x = x
        self.y = y
        self.satiety = satiety
        self.color = (255, 255, 0)
        Game.list_of_foods.append(self)


life = Creature()
food = Food(x=1, y=7)
food = Food(x=5, y=12)
food = Food(x=9, y=2)
for i in range(1):
    obstacle = Obstacle(5, 8, 2, 3)
Game.init_game()

while Game.run:
    pygame.time.delay(75)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.run = False
            break
        elif event.type == pygame.VIDEORESIZE:
            Game.window_width, Game.window_height = event.w, event.h
            Game.window = pygame.display.set_mode((Game.window_width, Game.window_height), pygame.RESIZABLE)
    
    Game.window.fill((255, 255, 255))
    Game.loop()
    Game.draw_obstacles()
    Game.draw_grid()
    Game.draw_creatures()
    Game.draw_foods()
    pygame.display.update()

pygame.quit()
