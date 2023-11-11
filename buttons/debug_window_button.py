from buttons.button import Button


class DebugWindowButton(Button):
    def action(self):
        print("!!!!!!!!!")
        return super().action()
