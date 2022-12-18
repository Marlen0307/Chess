from enum import Enum

figures = {0: 'Pawn', 1: 'Rook', 2: 'Knight', 3: 'Queen', 4: 'King', 5: 'Bishop'}


class Directions(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    TOP = 'TOP'
    BOTTOM = "BOTTOM"


extremes = {
    Directions.LEFT: 0,
    Directions.RIGHT: 7,
    Directions.BOTTOM: 0,
    Directions.TOP: 7,
}
