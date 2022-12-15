from models import Postion
from models.ChessBoard import get_position, get_x_index, get_x
from models.ChessFigure import ChessFigure


class Pawn(ChessFigure):
    # returns None if forward position is occupied
    def get_forward_move(self):
        y = int(self.position.y) + self.direction * 1
        pos = get_position(self.position.x, y)
        if pos.occupied:
            return None
        return pos

    # returns array of possible positions for diagonal movement. If no possible moves returns empty array
    def get_diagonal_move(self):
        y = int(self.position.y) + self.direction * 1
        x1 = get_x(get_x_index(self.position.x) + 1)
        x2 = get_x(get_x_index(self.position.x) - 1)
        moves = []
        for x in [x1, x2]:  # Pawn could go either diagonally right or left
            pos: Postion = get_position(x, y)
            if pos.occupied and pos.chess_figure.color != self.color:  # only if position is occupied and the figure is enemy that is a possible move
                moves.append(pos)
        return moves

    def __init__(self, color: str, title: str, position: Postion, direction):
        super().__init__(color, title, position, direction)

    def get_next_move(self):
        moving_options = []
        forward_position = self.get_forward_move()
        if forward_position is not None:
            moving_options.append(forward_position)
        for pos in self.get_diagonal_move():
            moving_options.append(pos)
        if len(moving_options) > 0:
            print("Select your next move: \n")
            for i in range(len(moving_options)):
                print(str(i) + " : " + moving_options[i].to_string())
            new_pos = moving_options[int(input())]
            super().move(new_pos)
