import os
import numpy as np
import math
import random
from Board import Board
from Decks import Decks
from Player import Player


class Game:
    def __init__(self):
        self.init_counters()
        self.init_players()

    def init_counters(self):
        self.square = dict()
        self.brown = 0
        self.cyan = 0
        self.pink = 0
        self.orange = 0
        self.red = 0
        self.yellow = 0
        self.green = 0
        self.blue = 0
        self.station = 0
        self.utility = 0
        self.community = 0
        self.chance = 0

    def init_players(self):
        self.players = []
        for i in range(random.randint(2, 10)):
            self.players.append(Player())

    def Play(self):
        for i in range(random.randint(10, 100)):
            self.round()

    def round(self):
        for i in range(len, self.players):
            self.turn(i)

    def turn(self, playerID):
        if self.players[playerID].get_state():
            if Player.rolls_dice()[1]:
                self.players[playerID].out_of_jail()
        else:
            for i in range(3):
                roll = Player.rolls_dice()
                pos = self.players[playerID].get_position()
                self.players[playerID].set_position(Board.normalise_number(pos + roll))
                if roll[1] and i == 3:
                    # Go straight to jail.
                    self.players[playerID].set_position(Board.getJail())
                    self.players[playerID].jail = True
                else:
                    self.players[playerID].set_position(Board.normalise_number(pos + roll))

                # Do wadever in turn
                # Set counter


                if not roll[1]:
                    # End turn
                    break

        def go_to_jail(self, playerID):
            self.players[playerID].set_position(Board.getJail())
            # Check if own any card.

    def print_stats(self):
        pass


if __name__ == "__main__":

    # windows terminal will return nt
    # mac and linux terminals will return posix
    # pause so user can see printouts
    if os.name == "nt":
        os.system("pause")
