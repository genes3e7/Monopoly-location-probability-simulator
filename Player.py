import random
from Board import Board


class Player:
    def __init__(self):
        self.position = 0
        self.jail = False
        self.out_of_jail_free = None

    def get_position(self):
        return self.position

    def set_position(self, n):
        self.position = Board().normalise_number(n)

    def get_state(self):
        return self.jail

    def advance_to_go(self):
        self.position = Board().getGo()

    def to_illinois(self):
        self.position = Board().getIllinois()

    def to_charles(self):
        self.position = Board().getCharles()
    def to_reading(self):
        self.position = Board().getReading()
    def to_boardwalk(self):
        self.position = Board().getBoardwalk()
    def back_three(self):
        self.position = Board().normalise_number(self.position - 3)

    def next_station(self):
        self.position = Board().next_station(self.position)
    def next_utility(self):
        self.position = Board().next_utility(self.position)

    def go_to_jail(self):
        self.position = Board().getJail()
        self.jail = True

    def out_of_jail(self):
        self.jail = False

    def get_out_of_jail_card(self, deck):
        self.out_of_jail_free = deck

    def return_out_of_jail_card(self):
        self.out_of_jail_free = None
    
    def card_check(self):
        return self.out_of_jail_free

    def rolls_dice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1 + die2, die1 == die2
