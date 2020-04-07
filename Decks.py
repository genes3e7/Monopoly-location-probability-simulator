import random


class Decks:
    def __init__(self):
        self.community_deck = random.shuffle(list(i for i in range(17)))
        self.chance_deck = random.shuffle(list(i for i in range(17)))
        self.init_names()
        self.chance = 0
        self.community = 0

    def init_names(self):
        self.community_deck_names = {
            0: "Advance to Go. (Collect $200)",
            1: "Bank error in your favor. Collect $200",
            2: "Doctor's fees. Pay $50.",
            3: "From sale of stock you get $50",
            4: "Get Out of Jail Free",
            5: "Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.",
            6: "Grand Opera Night. Collect $50 from every player for opening night seats.",
            7: "Holiday Fund matures. Receive $100.",
            8: "Income tax refund. Collect $20.",
            9: "It's your birthday. Collect $10 from every player.",
            10: "Life insurance matures – Collect $100",
            11: "Hospital Fees. Pay $50.",
            12: "School fees. Pay $50.",
            13: "Receive $25 consultancy fee.",
            14: "You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.",
            15: "You have won second prize in a beauty contest. Collect $10.",
            16: "You inherit $100."
        }
        self.chance_deck_names = {
            1: "Advance to Go. (Collect $200)",
            2: "Advance to Illinois Ave. If you pass Go, collect $200.",
            3: "Advance to St. Charles Place. If you pass Go, collect $200.",
            4: "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown.",
            5: "Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.",
            6: "Bank pays you dividend of $50.",
            7: "Get out of Jail Free. This card may be kept until needed, or traded/sold.",
            8: "Go Back Three Spaces.",
            9: "Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.",
            10: "Make general repairs on all your property: For each house pay $25, For each hotel pay $100.",
            11: "Pay poor tax of $15",
            12: "Take a trip to Reading Railroad.",
            13: "Take a walk on the Boardwalk. Advance token to Boardwalk.",
            14: "You have been elected Chairman of the Board. Pay each player $50.",
            15: "Your building and loan matures. Receive $150.",
            16: "You have won a crossword competition. Collect $100."
        }

    def get_names(self, deck, id):
        if deck == "chance":
            return self.chance_deck_names[id]
        return self.community_deck_names[id]

    def draw_communityDeck(self):
        ans = self.community_deck.pop(0)
        if ans != 4:
            self.community_deck.append(ans)
        return ans

    def draw_chanceDeck(self):
        ans = self.chance_deck.pop(0)
        if ans != 7:
            self.chance_deck.append(ans)
        return ans

    def return_community(self):
        self.community_deck.append(4)

    def return_chance(self):
        self.chance_deck.append(7)
