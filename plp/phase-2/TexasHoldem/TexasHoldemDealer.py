__author__ = 'bogdan.cornianu'
from dealer import Dealer
from player import Player


def main():
    players_list = []
    number_of_players = input('Number of players: ')

    if number_of_players in range(2, 10):
        card_dealer = Dealer()

        for player in range(number_of_players):
            card_player = Player()
            players_list.append(card_player)
            card_dealer.deal_hand_to_player(card_player)

        for player in players_list:
            print 'Cards for player ' + str(players_list.index(player) + 1) + ':'
            for card in player.get_cards_in_hand():
                print card
            print '-------------------------------'

        print ''
        print 'Table hand of 5 cards: '
        card_dealer.deal_hand_to_board()

    else:
        print 'Invalid number of players.'

main()