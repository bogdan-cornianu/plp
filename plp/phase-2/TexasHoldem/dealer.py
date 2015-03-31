__author__ = 'bogdan.cornianu'
from player import Player
from deck import Deck
from random import randint


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)
        self.card_deck = Deck()
        self.card_deck.shuffle_deck()

    def deal_hand_to_player(self, to_player):
        to_player.add_card_to_hand(self.card_deck.get_card_by_position(randint(1, 51)))
        to_player.add_card_to_hand(self.card_deck.get_card_by_position(randint(1, 51)))

    def deal_hand_to_board(self):
        for card in range(4):
            print self.card_deck.get_random_card()
