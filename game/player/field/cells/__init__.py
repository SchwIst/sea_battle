from colorama import Fore, Back
from colorama.ansi import AnsiBack, AnsiFore

from game.utils import Display


class Cell(Display):
    foreground: AnsiFore
    background: AnsiBack
    text: str

    def __init__(self, text: str, foreground: AnsiFore, background: AnsiBack):
        self.text = text
        self.background = background
        self.foreground = foreground

    def __str__(self):
        return str(self.background) + \
               str(self.foreground) + \
               self.text + \
               Fore.RESET + Back.RESET

    def display(self):
        print(str(self), end='')


TYPES: dict[str, Cell] = {
    "empty": Cell(' ', Fore.WHITE, Back.WHITE),
    "ship": Cell('@', Fore.BLUE, Back.WHITE),
    "damaged": Cell('X', Fore.RED, Back.WHITE),
    "miss": Cell('•', Fore.BLACK, Back.WHITE),
    # TODO: add use of: "killed": Cell('X', Fore.WHITE, Back.RED),
    # TODO: add use of: "struck": Cell('0', Fore.YELLOW, Back.RESET),
    "selected": Cell('S', Fore.BLACK, Back.WHITE)
}