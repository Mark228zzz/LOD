import pygame
from vars import List


class Button:
    def __init__(self, game_window, x: int, y: int, width: int, height: int, inactive_color: tuple, active_color: tuple, text_color: tuple, text: str ='', font_size: int = 16):
        self.game_window = game_window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text_color = text_color
        self.text = text
        self.font_size = font_size

        List.buttons.append(self)

    def loop(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(self.game_window, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and not self.is_clicked:
                self.is_clicked = True
                if self.action is not None:
                    self.action()
            elif click[0] == 0:
                self.is_clicked = False
        else:
            pygame.draw.rect(self.game_window, self.inactive_color, (self.x, self.y, self.width, self.height))

    def draw(self):
        if self.text != '':
            font = pygame.font.SysFont("freesansbold", self.font_size)
            text_surf = font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
            self.game_window.blit(text_surf, text_rect)

    def action(self): ...
