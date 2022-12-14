from models.ChessBoard import ChessBoard
from models.Player import Player


class Game:
    players = [] * 2
    colors = {
        0: 'white',
        1: 'black'
    }

    def __init__(self):
        self.board = ChessBoard()
        self.ended = False
        self.init_players()

    def init_players(self):
        for number in [0, 1]:
            num_of_player = number + 1
            default_player_name = "Player " + str(num_of_player)
            player_name = input("Write name for " + default_player_name)
            if player_name == "":
                player_name = default_player_name
            player_color = self.colors[number]
            self.players.insert(number, Player(number, player_name, player_color))
