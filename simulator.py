import os
import numpy as np
import math
import random
from Board import Board
from Decks import Decks
from Player import Player
import concurrent.futures


class Game:
    def __init__(self):
        self.init_counters()
        self.init_players()
        self.deck = Decks()

    def init_counters(self):
        self.square = dict()
        for i in range(len(Board().names)):
            self.square[i] = 0
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
        for i in range(random.randint(10,100)):
            self.round()

    def round(self):
        for i in range(len(self.players)):
            self.turn(i)

    def turn(self, playerID):
        if self.players[playerID].get_state():
            if Player().rolls_dice()[1]:
                self.players[playerID].out_of_jail()
        else:
            jailed = False
            for i in range(3):
                roll = self.players[playerID].rolls_dice()
                pos = self.players[playerID].get_position()
                if roll[1] and i == 3:
                    # Go straight to jail.
                    self.go_to_jail(playerID)
                    self.update_counter(pos)
                    break
                else:
                    pos = Board().normalise_number(pos + roll[0])
                    self.players[playerID].set_position(pos)
                    self.update_counter(pos)
                    # Do wadever in turn
                    if Board().communityCheck(pos):
                        card = self.deck.draw_communityDeck()
                        if card == 4:
                            self.players[playerID].get_out_of_jail_card(
                                "community")
                        elif card == 0:
                            self.players[playerID].advance_to_go()
                        elif card == 5:
                            self.go_to_jail(playerID)
                    elif Board().chanceCheck(pos):
                        card = self.deck.draw_chanceDeck()
                        if card == 6:
                            self.players[playerID].get_out_of_jail_card(
                                "chance")
                        elif card == 0:
                            self.players[playerID].advance_to_go()
                        elif card == 1:
                            self.players[playerID].to_illinois()
                        elif card == 2:
                            self.players[playerID].to_charles()
                        elif card == 3:
                            self.players[playerID].next_utility()
                        elif card == 4:
                            self.players[playerID].next_station()
                        elif card == 7:
                            self.players[playerID].back_three()
                        elif card == 8:
                            self.go_to_jail(playerID)
                        elif card == 11:
                            self.players[playerID].to_reading()
                        elif card == 12:
                            self.players[playerID].to_boardwalk()

                    if pos != self.players[playerID].get_position():
                        self.update_counter(
                            self.players[playerID].get_position())

                if not roll[1]:
                    # End turn
                    break
                if jailed:
                    self.go_to_jail(playerID)
                    break

    def update_counter(self, pos):
        self.square[pos] += 1
        if Board().brownCheck(pos):
            self.brown += 1
        elif Board().cyanCheck(pos):
            self.cyan += 1
        elif Board().pinkCheck(pos):
            self.pink += 1
        elif Board().orangeCheck(pos):
            self.orange += 1
        elif Board().redCheck(pos):
            self.red += 1
        elif Board().yellowCheck(pos):
            self.yellow += 1
        elif Board().greenCheck(pos):
            self.green += 1
        elif Board().blueCheck(pos):
            self.blue += 1
        elif Board().stationCheck(pos):
            self.station += 1
        elif Board().utilityCheck(pos):
            self.utility += 1
        elif Board().communityCheck(pos):
            self.community += 1
        elif Board().chanceCheck(pos):
            self.chance += 1

    def go_to_jail(self, playerID):
        self.players[playerID].set_position(Board().getJail())
        # Check if own any card.
        check = self.players[playerID].card_check()
        if check:
            self.players[playerID].return_out_of_jail_card()
            if check == "chance":
                self.deck.return_chance()
            else:
                self.deck.return_community()
        else:
            self.players[playerID].go_to_jail()

    def get_details(self):
        return(
            list(self.square.values()),
            self.brown,
            self.cyan,
            self.pink,
            self.orange,
            self.red,
            self.yellow,
            self.green,
            self.blue,
            self.station,
            self.utility,
            self.community,
            self.chance
        )

def print_stats(squares, brown, cyan, pink, orange, red, yellow, green, blue, station, utility, community, chance):
    total = sum(squares)
    print("{:<3}: {:^43}:{:^8}:{:^8}:{:>6}".format("idx", "name", "Count", "Total", "(%)"))
    for i in range(len(Board().names)):
        print("{:<3}: {:^43}:{:^8}:{:^8}:{:>6}".format(i, Board().names[i], squares[i], total, round((squares[i] / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("Type", "Count", "Total", "(%)"))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("brown", brown, total, round((brown / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("cyan", cyan, total, round((cyan / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("pink", pink, total, round((pink / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("orange", orange, total, round((orange / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("red", red, total, round((red / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("yellow", yellow, total, round((yellow / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("green", green, total, round((green / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("blue", blue, total, round((blue / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("station", station, total, round((station / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("utility", utility, total, round((utility / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("community", community, total, round((community / total) * 100, 2)))
    print("{:^9}:{:^8}:{:^8}:{:>6}".format("chance", chance, total, round((chance / total) * 100, 2)))

def play_game():
    new_game = Game()
    new_game.Play()
    return new_game.get_details()

if __name__ == "__main__":
    temp = [[0 for i in range(40)], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        threads = []
        for i in range(1000):
            threads.append(executor.submit(play_game))
        for i in threads:
            for j in range(len(i.result()[0])):
                temp[0][j] += i.result()[0][j]
            for j in range(1, len(i.result())):
                temp[j] += i.result()[j]

    print_stats(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12])
    # windows terminal will return nt
    # mac and linux terminals will return posix
    # pause so user can see printouts
    if os.name == "nt":
        os.system("pause")
