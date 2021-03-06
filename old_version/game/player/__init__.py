from typing import Union, Callable

from old_version.game.player.field import TYPES
from old_version.game.player.field import Field
from old_version.game.player.field import Ship
from old_version.game.utils import Display, move_print, FILE_TEMPLATE
from .read_input import Input
from .shooter import Shooter


class Player(Shooter, Display, Input):
    chosen_position_x: int
    chosen_position_y: int

    field: Field
    enemy_field: Field
    enemy_field_hidden: Field

    moving_ships: bool = True

    def __init__(self, our_field: Field, enemy_field: Field):
        self.field = our_field

        self.enemy_field = enemy_field
        self.enemy_field_hidden = enemy_field.clone()

        self.chosen_position_x = 1
        self.chosen_position_y = 1

    def get_enemy_field_hidden(self) -> Field:
        return self.enemy_field_hidden

    def get_enemy_field(self):
        return self.enemy_field

    def get_shoot_coordinates(self) -> tuple[int, int]:
        return self.chosen_position_y, self.chosen_position_x

    def display(self):
        self.field.display()
        self.enemy_field_hidden.display()

        field_position_x, field_position_y = self.enemy_field_hidden.get_position()

        cursor_x = self.chosen_position_x + field_position_x
        cursor_y = self.chosen_position_y + field_position_y

        move_print(str(TYPES["selected"]), cursor_x, cursor_y)

    def react_to_keys(self, pressed_key: bytes) -> Union[tuple[int, int], Callable[[Ship], None], bool]:
        _match: dict[bytes, Union[tuple[int, int], Callable[[Ship], None]], bool] = {
            b"w": (0, -1),
            b"a": (-1, 0),
            b"s": (0, 1),
            b"d": (1, 0),
            b"r": lambda x: x.rotate(),
            b"e": True
        }

        return _match[pressed_key]

    def move_cursor(self, vector: tuple[int, int]):
        if self.chosen_position_x + vector[0] not in range(
                FILE_TEMPLATE["fields"][1]["size"][0]
        ) or self.chosen_position_y + vector[1] not in range(
            FILE_TEMPLATE["fields"][1]["size"][1]
        ):
            return

        self.chosen_position_x += vector[0]
        self.chosen_position_y += vector[1]
