from cells import Cell, CellTypes
from ship import Ship
from utils import Display, move_print


class Field(Display):
    _width: int
    _height: int

    _x: int = 0
    _y: int = 0

    ships: list[Ship]

    cells: list[list[Cell]]

    def __init__(self, width: int, height: int, x: int, y: int):
        self._width = width
        self._height = height

        self._x = x
        self._y = y

        self.cells = []

    def _empty(self):
        for i in range(self._height):
            self.cells.append([])
            for j in range(self._width):
                self.cells[i].append(CellTypes["empty"])

    def fill(self):
        self._empty()

    def print(self):
        for x, row in enumerate(self.cells):
            for y, element in enumerate(row):
                lx, ly = self._x + x, self._y + y

                move_print(str(element), lx, ly)
