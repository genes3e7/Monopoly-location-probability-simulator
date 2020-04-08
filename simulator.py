import os
import time
import random
from Board import Board
from Decks import Decks
from Player import Player
import concurrent.futures

PROCESSES = 100
THREADS = 1000

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
                    elif pos == 30:
                        self.go_to_jail(playerID)

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

def print_stats(data):
    squares = data[0]
    brown, cyan, pink, orange = data[1], data[2], data[3], data[4]
    red, yellow, green, blue = data[5], data[6], data[7], data[8]
    station, utility, community, chance = data[9], data[10], data[11], data[12]

    SQUARE = lambda a, b, c, d : "{:<3}: {:^43}:{:^8}:{:>6}".format(a, b, c, d)
    TYPE = lambda a, b, c : "{:^9}:{:^8}:{:>6}".format(a, b, c)

    print("No of Games: {}".format(PROCESSES * THREADS))
    total = sum(squares)
    print("Total Lands: {}\n".format(total))

    print("{:^64}\n{}".format("Individual Squares", "-" * 64))
    print(SQUARE("idx", "name", "Count", "(%)"))
    print("-" * 64)
    for i in range(len(Board().names)):
        print(SQUARE(i, Board().names[i], squares[i], round((squares[i] / total) * 100, 2)))

    print("\n{:^25}\n{}".format("Type", "-" * 25))
    print(TYPE("Type", "Count", "(%)"))
    print("-" * 25)
    print(TYPE("brown", brown, round((brown / total) * 100, 2)))
    print(TYPE("cyan", cyan, round((cyan / total) * 100, 2)))
    print(TYPE("pink", pink, round((pink / total) * 100, 2)))
    print(TYPE("orange", orange, round((orange / total) * 100, 2)))
    print(TYPE("red", red, round((red / total) * 100, 2)))
    print(TYPE("yellow", yellow, round((yellow / total) * 100, 2)))
    print(TYPE("green", green, round((green / total) * 100, 2)))
    print(TYPE("blue", blue, round((blue / total) * 100, 2)))
    print(TYPE("station", station, round((station / total) * 100, 2)))
    print(TYPE("utility", utility, round((utility / total) * 100, 2)))
    print(TYPE("community", community, round((community / total) * 100, 2)))
    print(TYPE("chance", chance, round((chance / total) * 100, 2)))

def single_process():
    temp = [[0 for i in range(40)], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        threads = []
        for i in range(THREADS):
            threads.append(executor.submit(play_game))
        for i in threads:
            for j in range(len(i.result()[0])):
                temp[0][j] += i.result()[0][j]
            for j in range(1, len(i.result())):
                temp[j] += i.result()[j]

    return temp

def play_game():
    new_game = Game()
    new_game.Play()
    return new_game.get_details()

if __name__ == "__main__":
    start_time = time.time()
    print("Program Start")
    
    data = [[0 for i in range(40)], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        processes = []
        for i in range(PROCESSES):
            processes.append(executor.submit(single_process))
        for i in processes:
            for j in range(len(i.result()[0])):
                data[0][j] += i.result()[0][j]
            for j in range(1, len(i.result())):
                data[j] += i.result()[j]

    print_stats(data)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    # windows terminal will return nt
    # mac and linux terminals will return posix
    # pause so user can see printouts
    if os.name == "nt":
        os.system("pause")
