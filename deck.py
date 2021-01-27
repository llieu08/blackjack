import random
from card import *


class Deck:
    def __init__(self, decks=1):
        self.decks = decks
        self.cards = []
        for i in range(decks):
            for suit in range(4):
                for value in range(1, 14):
                    self.cards.append(Card(suit, value))

    def shuffle(self):
        return random.shuffle(self.cards)
