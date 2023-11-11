from buttons.button import Button
from vars import List


class DebugWindowButton(Button):
    def __init__(self, game_window, x: int, y: int, width: int, height: int, inactive_color: tuple, active_color: tuple, text_color: tuple, text: str = '', font_size: int = 16, debug_window: object = None):
        self.debug_window = debug_window
        super().__init__(game_window, x, y, width, height, inactive_color, active_color, text_color, text, font_size)

    def action(self):
        for window in List.windows:
            if window.name == 'Debug Window':
                window.visible = not window.visible
                break
        return super().action()
