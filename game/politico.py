from .game import BaseGame
from deck.politico_deck import PoliticoDeck


class Politico(BaseGame):

    game_name = 'Politico'
    cards_per_hand = 1

    def __init__(self, players_filename):
        super(Politico, self).__init__(players_filename)
        self.set_deck(PoliticoDeck(self.n_players))

    def play(self):
        self.deck.shuffle()
        self.deal_hands()
        self.notify_players()
