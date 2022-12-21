from models import Postion
from models.ChessBoard import get_position, get_x_index, get_x
from models.ChessFigure import ChessFigure


class Pawn(ChessFigure):

    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)

    # returns array with possible moves, empty array if no possible moves
    def get_forward_move(self):
        steps = [1]
        if not self.get_moved():  # first move of Pawn can be double step
            steps.append(2)
        possible_moves = []
        for step in steps:
            y = int(self.position.y) + self.direction * step
            pos = get_position(self.position.x, y)
            if not pos.occupied:
                possible_moves.append(pos)
        return possible_moves

    # returns array of possible positions for diagonal movement. If no possible moves returns empty array
    def get_diagonal_move(self):
        y = int(self.position.y) + self.direction * 1
        x1 = get_x(get_x_index(self.position.x) + 1)
        x2 = get_x(get_x_index(self.position.x) - 1)
        moves = []
        for x in [x1, x2]:  # Pawn could go either diagonally right or left
            if x is not None:
                pos: Postion = get_position(x, y)
                if pos.occupied and pos.chess_figure.color != self.color:  # only if position is occupied and the figure is enemy that is a possible move
                    moves.append(pos)
        return moves

    def get_moves(self):
        return self.get_forward_move() + self.get_diagonal_move()

    def get_moving_options(self):
        moving_options = self.get_moves()
        self.get_next_move(moving_options)
