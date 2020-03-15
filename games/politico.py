from base.game import BaseGame
from base.deck import BaseDeck


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


class PoliticoDeck(BaseDeck):

    politician_str = 'Politico'
    commoner_str = 'Pueblo'

    def __init__(self, n_players, n_politicians=None):
        self.cards = self.create_deck(n_players, n_politicians)

    def create_deck(self, n_players, n_politicians=None):
        if not n_politicians:
            if n_players == 4:
                n_politicians = 1
            elif n_players <= 6:
                n_politicians = 2
            elif n_players <=9:
                n_politicians = 3
            else:
                n_politicians = 4
        n_commoners = n_players - n_politicians
        return [self.politician_str] * n_politicians\
            + [self.commoner_str] * n_commoners
