from base.game import BaseGame
from base.deck import BaseDeck


class Insider(BaseGame):

    game_name = 'Insider'
    cards_per_hand = 1

    def __init__(self, players_filename):
        super(Insider, self).__init__(players_filename)
        self.set_deck(InsiderDeck(self.n_players))

    def play(self):
        self.deck.shuffle()
        self.deal_hands()
        self.notify_players()


class InsiderDeck(BaseDeck):

    insider_str = 'Insider'
    master_str = 'Master'
    common_str = 'Common'

    def __init__(self, n_players):
        self.cards = self.create_deck(n_players)

    def create_deck(self, n_players):
        n_commons = n_players - 2
        deck = [self.insider_str, self.master_str]
        deck += [self.common_str] * n_commons
        return deck
