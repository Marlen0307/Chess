import string
from typing import Union

from models.ChessFigure import ChessFigure


class Position:
    def __init__(self, y_pos: Union[str, int], x_pos: Union[str, int], figure: Union[ChessFigure, None]):
        self.y = str(y_pos)
        self.x = str(x_pos)
        self.occupied = figure is not None
        self.chess_figure = figure

    def set_chess_figure(self, new_figure: ChessFigure):
        self.chess_figure = new_figure
        self.set_occupied(new_figure is not None)

    def set_occupied(self, new_state: bool):
        self.occupied = new_state

    def to_string(self):
        return str(self.y) + str(self.x)
