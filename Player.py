import random
from Board import Board

class Player:
    def __init__(self):
        self.position = 0
        self.jail = False
        self.out_of_jail_free = 0

    def get_position(self):
        return self.position

    def set_position(self, n):
        self.position = Board.normalise_number(n)

    def get_state(self):
        return self.jail

    def go_to_jail(self):
        self.jail = True
    def out_of_jail(self):
        self.jail = False

    def get_out_of_jail_card(self, deck):
        self.out_of_jail_free = deck

    def return_out_of_jail_card(self, deck):
        temp = self.out_of_jail_free
        self.out_of_jail_free = 0

        return temp

    def rolls_dice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1 + die2, die1 == die2
