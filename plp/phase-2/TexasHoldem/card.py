__author__ = 'bogdan.cornianu'


class Card:

    def __init__(self, rank, suit):
        if rank in ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
            self.rank = rank
        else:
            print 'Invalid rank: ' + rank

        if suit in ['Spades', 'Hearts', 'Clubs', 'Diamonds']:
            self.suit = suit
        else:
            print 'Invalid suit: ' + suit

    def __str__(self):
        return self.rank + ' of ' + self.suit