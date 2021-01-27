class Card:
    suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    values = ['0', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.values[self.value] + ' of ' + self.suits[self.suit]
