__author__ = 'bogdan.cornianu'


class Player:

    def __init__(self):
        self.cards_in_hand = []

    def get_cards_in_hand(self):
        return self.cards_in_hand

    def add_card_to_hand(self, card):
        self.cards_in_hand.append(card)