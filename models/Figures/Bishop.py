from Constants import Directions, extremes, CrossDirections
from models import Postion
from models.ChessBoard import get_x_index, get_y_index, get_position, ChessBoard
from models.ChessFigure import ChessFigure, is_position_valid


def get_top_right_left_bottom_moves(figure, position, cross_direction):
    x = position.x
    y = position.y
    x_index = get_x_index(x)
    y_index = get_y_index(y)

    def get_condition():
        condition = x_index <= extremes[Directions.RIGHT] and y_index <= extremes[Directions.TOP]
        if cross_direction == CrossDirections.LEFT_BOTTOM:
            condition = x_index >= extremes[Directions.LEFT] and y_index >= extremes[Directions.BOTTOM]
        return condition

    direction = 1 if cross_direction == CrossDirections.RIGHT_TOP else -1
    moves_arr = []

    while get_condition():
        pos = get_position(ChessBoard.x_positions[x_index], ChessBoard.y_positions[y_index])
        if is_position_valid(figure, pos):
            moves_arr.append(pos)
            x_index = x_index + direction * 1
            y_index = y_index + direction * 1
            continue
        x_index = x_index + direction * 1
        y_index = y_index + direction * 1
        break_condition = pos.to_string() != figure.position.to_string()
        if break_condition:
            break
    return moves_arr


class Bishop(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)

    def get_all_moving_options(self):
        top_right_moves = get_top_right_left_bottom_moves(self, self.position, CrossDirections.RIGHT_TOP)
        bottom_left_moves = get_top_right_left_bottom_moves(self, self.position, CrossDirections.LEFT_BOTTOM)
        return top_right_moves + bottom_left_moves

    def get_moving_options(self):
        moving_options = self.get_all_moving_options()
        self.get_next_move(moving_options)
