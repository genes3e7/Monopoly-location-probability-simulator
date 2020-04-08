class Board:
    def __init__(self):
        self.names = {
            0: "Go",
            1: "Old Kent or Mediteranean Avenue",
            2: "Community Chest",
            3: "Whitechapel Road or Baltic Avenue",
            4: "Income Tax",
            5: "Kings Cross Station or reading railroad",
            6: "The Angel, Islington or Oriental Avenue",
            7: "Chance",
            8: "Euston Road or Vermont Avenue",
            9: "Pentonville Road or Connecticut avenue",
            10: "Jail/Just Visiting",
            11: "Pall Mall or St. Charles Place",
            12: "Electric Company",
            13: "Whitehall or States Avenue",
            14: "Northumb'nd Avenue or Virginia Avenue",
            15: "Marylebone Station or Pennsylvania Railroad",
            16: "Bow Street or St. James Place",
            17: "Community Chest",
            18: "Marlborough Street or Tennessee Avenue",
            19: "Vine Street or New York Avenue",
            20: "Free Parking",
            21: "Strand or Kentucky Avenue",
            22: "Chance",
            23: "Fleet Street or Indiana Avenue",
            24: "Trafalgar Square or Illinois Avenue",
            25: "Fenchurch St. Station or B. & O. Railroad",
            26: "Leicester Square or Atlantica Avenue",
            27: "Coventry Street or Ventnor Avenue",
            28: "Water Works",
            29: "Piccadilly or Marvin Gardens",
            30: "Go to Jail",
            31: "Regent Street or Pacific Avenue",
            32: "Oxford Street or Naroth Carolina Avenue",
            33: "Community Chest",
            34: "Bond Street or Pennsylvania Avenue",
            35: "Liverpool St. Station or Short Line",
            36: "Chance",
            37: "Park Lane or Park Place",
            38: "Super Tax",
            39: "May Fair or Boardwalk"
        }

    def brownCheck(self, n):
        return n in (1, 3)
    def cyanCheck(self, n):
        return n in (6, 8, 9)
    def pinkCheck(self, n):
        return n in (11, 13, 14)
    def orangeCheck(self, n):
        return n in (16, 18, 19)
    def redCheck(self, n):
        return n in (21, 23, 24)
    def yellowCheck(self, n):
        return n in (26, 27, 29)
    def greenCheck(self, n):
        return n in (31, 32, 34)
    def blueCheck(self, n):
        return n in (37, 39)
    def stationCheck(self, n):
        return n in (5, 15, 25, 35)
    def utilityCheck(self, n):
        return n in (12, 28)

    def next_station(self, n):
        if 35 < n < len(self.names) or 0 <= n <= 5:
            return 5
        elif 5 < n <= 15:
            return 15
        elif 15 < n <= 25:
            return 25
        else:
            return 35
    def next_utility(self, n):
        if 12 < n <= 28:
            return 28
        else:
            return 12

    def communityCheck(self, n):
        return n in (2, 17, 33)

    def chanceCheck(self, n):
        return n in (7, 22, 36)

    def normalise_number(self, n):
        return n % 40

    def getJail(self):
        return 10

    def getGo(self):
        return 0

    def getIllinois(self):
        return 24
    def getCharles(self):
        return 11
    def getReading(self):
        return 5
    def getBoardwalk(self):
        return 39