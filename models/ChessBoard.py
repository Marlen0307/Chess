from models.Figures.Bishop import Bishop
from models.Figures.King import King
from models.Figures.Knight import Knight
from models.Figures.Queen import Queen
from models.Postion import Position
from models.Figures.Rook import Rook

initial_figures_mapping = {
    '1A': Rook,
    '8A': Rook,
    '1H': Rook,
    '8H': Rook,
    '1B': Knight,
    '8B': Knight,
    '1G': Knight,
    '8G': Knight,
    '1C': Bishop,
    '8C': Bishop,
    '1F': Bishop,
    '8F': Bishop,
    '1D': Queen,
    '8D': Queen,
    '1E': King,
    '8E': King
}


def fill_board():
    for number in ChessBoard.y_positions:
        positions = [] * len(ChessBoard.x_positions)
        for letter in ChessBoard.x_positions:
            positions.append(Position(number, letter, None))
        ChessBoard.positions.insert(number - 1, positions)


def get_position(x, y) -> Position:
    y_index = ChessBoard.y_positions.index(y)
    x_index = ChessBoard.x_positions.index(x)
    return ChessBoard.positions[y_index][x_index]


def get_x_index(x: str):
    return ChessBoard.x_positions.index(x)


def get_x(x_index: int):
    try:
        return ChessBoard.x_positions[x_index]
    except IndexError:
        return None


class ChessBoard:
    x_positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    y_positions = [1, 2, 3, 4, 5, 6, 7, 8]
    positions = [] * len(y_positions)

    def __init__(self):
        fill_board()
