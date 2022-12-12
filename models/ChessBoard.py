from models.Postion import Position


def fill_board():
    for number in ChessBoard.y_positions:
        positions = [] * len(ChessBoard.x_positions)
        for letter in ChessBoard.x_positions:
            positions.append(Position(number, letter, None))
        ChessBoard.positions.insert(number - 1, positions)


class ChessBoard:
    x_positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    y_positions = [1, 2, 3, 4, 5, 6, 7, 8]
    positions = [] * len(y_positions)

    def __init__(self):
        fill_board()
