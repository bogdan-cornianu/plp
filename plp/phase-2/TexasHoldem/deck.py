__author__ = 'bogdan.cornianu'
import card
from random import shuffle, randint


class Deck:

    def __init__(self):
        self.deck = []
        self.deck.append(card.Card('Ace', 'Clubs'))
        self.deck.append(card.Card('Ace', 'Diamonds'))
        self.deck.append(card.Card('Ace', 'Hearts'))
        self.deck.append(card.Card('Ace', 'Spades'))
        self.deck.append(card.Card('2', 'Clubs'))
        self.deck.append(card.Card('2', 'Diamonds'))
        self.deck.append(card.Card('2', 'Hearts'))
        self.deck.append(card.Card('2', 'Spades'))
        self.deck.append(card.Card('3', 'Clubs'))
        self.deck.append(card.Card('3', 'Diamonds'))
        self.deck.append(card.Card('3', 'Hearts'))
        self.deck.append(card.Card('3', 'Spades'))
        self.deck.append(card.Card('4', 'Clubs'))
        self.deck.append(card.Card('4', 'Diamonds'))
        self.deck.append(card.Card('4', 'Hearts'))
        self.deck.append(card.Card('4', 'Spades'))
        self.deck.append(card.Card('5', 'Clubs'))
        self.deck.append(card.Card('5', 'Diamonds'))
        self.deck.append(card.Card('5', 'Hearts'))
        self.deck.append(card.Card('5', 'Spades'))
        self.deck.append(card.Card('6', 'Clubs'))
        self.deck.append(card.Card('6', 'Diamonds'))
        self.deck.append(card.Card('6', 'Hearts'))
        self.deck.append(card.Card('6', 'Spades'))
        self.deck.append(card.Card('7', 'Clubs'))
        self.deck.append(card.Card('7', 'Diamonds'))
        self.deck.append(card.Card('7', 'Hearts'))
        self.deck.append(card.Card('7', 'Spades'))
        self.deck.append(card.Card('8', 'Clubs'))
        self.deck.append(card.Card('8', 'Diamonds'))
        self.deck.append(card.Card('8', 'Hearts'))
        self.deck.append(card.Card('8', 'Spades'))
        self.deck.append(card.Card('9', 'Clubs'))
        self.deck.append(card.Card('9', 'Diamonds'))
        self.deck.append(card.Card('9', 'Hearts'))
        self.deck.append(card.Card('9', 'Spades'))
        self.deck.append(card.Card('10', 'Clubs'))
        self.deck.append(card.Card('10', 'Diamonds'))
        self.deck.append(card.Card('10', 'Hearts'))
        self.deck.append(card.Card('10', 'Spades'))
        self.deck.append(card.Card('Jack', 'Clubs'))
        self.deck.append(card.Card('Jack', 'Diamonds'))
        self.deck.append(card.Card('Jack', 'Hearts'))
        self.deck.append(card.Card('Jack', 'Spades'))
        self.deck.append(card.Card('Queen', 'Clubs'))
        self.deck.append(card.Card('Queen', 'Diamonds'))
        self.deck.append(card.Card('Queen', 'Hearts'))
        self.deck.append(card.Card('Queen', 'Spades'))
        self.deck.append(card.Card('King', 'Clubs'))
        self.deck.append(card.Card('King', 'Diamonds'))
        self.deck.append(card.Card('King', 'Hearts'))
        self.deck.append(card.Card('King', 'Spades'))

    def add_card(self, c):
        self.deck.append(c)

    def remove_card(self, c):
        self.deck.remove(c)

    def get_random_card(self):
        return self.deck[randint(1, 51)]

    def shuffle_deck(self):
        shuffle(self.deck)

    def sort_deck(self):
        self.deck.sort()

    def get_card_by_position(self, position):
        return self.deck[position]