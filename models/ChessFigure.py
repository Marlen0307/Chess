from models import Postion


class ChessFigure:

    def __init__(self, color: str, title: str, position: Postion, direction):
        self.position = position
        self.killed = False
        self.color = color
        self.title = title
        self.direction = direction

    def move(self, new_position: Postion):
        self.position.set_chess_figure(None)
        self.position = new_position
        if new_position.occupied:
            self.beat()
        new_position.set_chess_figure(self)
        print(self)
        print(new_position)

    def beat(self):  # TODO: IMPLEMENT BEAT METHOD
        pass

    def set_title(self, new_title: str):
        self.title = new_title

    def get_position(self):
        return self.position.to_string()
