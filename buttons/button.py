import pygame
from vars import List


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, inactive_color: tuple, active_color: tuple, text: str =''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text

        List.buttons.append(self)

    def loop(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and not self.is_clicked:
                self.is_clicked = True
                if self.action is not None:
                    self.action()
            elif click[0] == 0:
                self.is_clicked = False
        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))

    def draw(self, screen):
        if self.text != '':
            font = pygame.font.SysFont("freesansbold", 20)
            text_surf = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
            screen.blit(text_surf, text_rect)

    def action(self): ...
