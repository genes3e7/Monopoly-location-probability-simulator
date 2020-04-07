class Board:
    def __init__(self):
        pass

    def squares(self):
        self.names = {
            0: "Go",
            1: "Old Kent",
            2: "Community Chest",
            3: "Whitechapel Road",
            4: "Income Tax",
            5: "Kings Cross Station",
            6: "The Angel, Islington",
            7: "Chance",
            8: "Euston Road",
            9: "Pentonville Road",
            10: "Jail/Just Visiting",
            11: "Pall Mall",
            12: "Electric Company",
            13: "Whitehall",
            14: "Northumb'nd Avenue",
            15: "Marylebone Station",
            16: "Bow Street",
            17: "Community Chest",
            18: "Marlborough Street",
            19: "Vine Street",
            20: "Free Parking",
            21: "Strand",
            22: "Chance",
            23: "Fleet Street",
            24: "Trafalgar Square",
            25: "Fenchurch St. Station",
            26: "Leicester Square",
            27: "Coventry Street",
            28: "Water Works",
            29: "Piccadilly",
            30: "Go to Jail",
            31: "Regent Street",
            32: "Oxford Street",
            33: "Community Chest",
            34: "Bond Street",
            35: "Liverpool St. Station",
            36: "Chance",
            37: "Park Lane",
            38: "Super Tax",
            39: "May Fair"
        }
    def brownCheck(self, n):
        return n in (1, 3)
    def cyanCheck(self,n):
        return n in (6, 8, 9)
    def pinkCheck(self,n):
        return n in (11, 13, 14)
    def orangeCheck(self, n):
        return n in (16, 18, 19)
    def redCheck(self, n):
        return n in (21, 23, 24)
    def yellowCheck(self,n):
        return n in (26, 27, 29)
    def greenCheck(self, n):
        return n in (31, 32, 34)
    def blueCheck(self, n):
        return n in (37, 39)
    
    def stationCheck(self, n):
        return n in (5, 15, 25, 35)
    def utilityCheck(self, n):
        return n in (12, 28)

    def communityCheck(self, n):
        return n in (2,17,33)
    def chanceCheck(self, n):
        return n in (7, 22, 36)

    def normalise_number(self, n):
        return n % 40

    def getJail(self):
        return 10