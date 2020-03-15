from .deck import BaseDeck


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
