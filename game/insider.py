from .game import BaseGame
from deck.insider_deck import InsiderDeck


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
