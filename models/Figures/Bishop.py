from Constants import Directions, extremes, CrossDirections
from models import Postion
from models.ChessBoard import get_x_index, get_y_index, get_position, ChessBoard
from models.ChessFigure import ChessFigure


def get_top_right_left_bottom_moves(figure, position, cross_direction):
    x = position.x
    y = position.y
    initial_x_index = get_x_index(x)
    initial_y_index = get_y_index(y)

    def get_condition(x_index, y_index):
        condition = x_index <= extremes[Directions.RIGHT] and y_index <= extremes[Directions.TOP]
        if cross_direction == CrossDirections.LEFT_BOTTOM:
            condition = x_index >= extremes[Directions.LEFT] and y_index >= extremes[Directions.BOTTOM]
        return condition

    direction = 1 if cross_direction == CrossDirections.RIGHT_TOP else -1

    return get_diagonal_moves_by_dir(figure, direction, direction, initial_x_index, initial_y_index, get_condition)


def get_diagonal_moves_by_dir(figure, x_direction, y_direction, x_index, y_index, get_condition):
    moves_arr = []

    while get_condition(x_index, y_index):
        pos = get_position(ChessBoard.x_positions[x_index], ChessBoard.y_positions[y_index])
        if figure.is_position_valid(pos):
            moves_arr.append(pos)
            x_index = x_index + x_direction * 1
            y_index = y_index + y_direction * 1
            if pos.occupied:  # if we come here a enemy is in this position which means that is the last valid position in that direction so we break the loop
                break
            continue
        x_index = x_index + x_direction * 1
        y_index = y_index + y_direction * 1
        break_condition = pos.to_string() != figure.position.to_string()
        if break_condition:  # if we come here the position is not valid and we should not consider any other position
            break

    return moves_arr


def get_top_left_right_bottom_moves(figure, position, cross_direction):
    x = position.x
    y = position.y
    initial_x_index = get_x_index(x)
    initial_y_index = get_y_index(y)

    y_direction = 1 if cross_direction == CrossDirections.LEFT_TOP else -1
    x_direction = 1 if cross_direction == CrossDirections.RIGHT_BOTTOM else -1

    def get_condition(x_index, y_index):
        condition = x_index >= extremes[Directions.LEFT] and y_index <= extremes[Directions.TOP]
        if cross_direction == CrossDirections.RIGHT_BOTTOM:
            condition = x_index <= extremes[Directions.RIGHT] and y_index >= extremes[Directions.BOTTOM]
        return condition

    return get_diagonal_moves_by_dir(figure, x_direction, y_direction, initial_x_index, initial_y_index, get_condition)


class Bishop(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)

    def get_moves(self):
        top_right_moves = get_top_right_left_bottom_moves(self, self.position, CrossDirections.RIGHT_TOP)
        bottom_left_moves = get_top_right_left_bottom_moves(self, self.position, CrossDirections.LEFT_BOTTOM)
        top_left_moves = get_top_left_right_bottom_moves(self, self.position, CrossDirections.LEFT_TOP)
        right_bottom_moves = get_top_left_right_bottom_moves(self, self.position, CrossDirections.RIGHT_BOTTOM)

        return top_right_moves + bottom_left_moves + top_left_moves + right_bottom_moves

    def get_moving_options(self):
        moving_options = self.get_moves()
        self.get_next_move(moving_options)
