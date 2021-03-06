from old_version.game.player.field.cells import Cell, TYPES
from old_version.game.player.field.ship import Ship
from old_version.game.utils import Display, move_print


class Field(Display):
    _width: int
    _height: int

    _x: int = 0
    _y: int = 0

    possible_ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    ships: list[Ship]  # TODO: MAKE PRIV

    cells: list[list[Cell]]  # TODO: MAKE PRIV

    def __init__(self, width: int, height: int, x: int, y: int):
        self._width = width
        self._height = height

        self._x = x
        self._y = y

        self.cells = []
        self.ships = []

        self.possible_ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    from ._ship_action import create_ship, rotate_last_ship, move_last_ship, not_intersect_padding, not_intersect, \
        pop_last_ship, bake_ships
    from ._creation import fill, _empty

    def get_cell(self, x: int, y: int):
        return self.cells[y][x]

    def set_cell(self, x: int, y: int, new_cell: Cell):
        self.cells[y][x] = new_cell

    def get_size(self) -> tuple[int, int]:
        return self._width, self._height

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y

    def clone(self):
        new = Field(self._width, self._height, self._x, self._y)

        new.fill()

        return new

    def display(self):
        for x, row in enumerate(self.cells):
            for y, element in enumerate(row):
                lx, ly = self._x + x, self._y + y

                move_print(str(element), lx, ly)

        for ship in self.ships:
            for x, y in ship.get_all_coordinates():
                move_print(str(TYPES["ship"]), x + self._x, y + self._y)
