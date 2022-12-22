import json

from Constants import figures
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
        self.loop()

    def init_players(self):
        for number in [0, 1]:
            num_of_player = number + 1
            default_player_name = "Player " + str(num_of_player)
            player_name = input("Write name for " + default_player_name + "\n")
            if player_name == "":
                player_name = default_player_name
            player_color = self.colors[number]
            self.players.insert(number, Player(number, player_name, player_color, self))

    def loop(self):
        while not self.ended:
            for player in self.players:
                game_can_go_on = player.look_for_check_on_your_king()
                if not game_can_go_on:
                    break
                print(player.name + "'s turn. Choose the figure you want to move")
                print(json.dumps(figures)[1:-1])  # print figure choices
                key = input()
                figure_to_be_moved = figures[int(key)]
                player.choose_moving_figure(figure_to_be_moved)

    def end(self, winner):
        self.ended = True
        if winner is not None:
            print(winner.name + " is the winner. Well played!")

