from base.game import BaseGame
from base.deck import NaipesDeck


class Envite(BaseGame):

    game_name = 'Envite'
    cards_per_hand = 3

    def __init__(self, players_filename):
        super(Envite, self).__init__(players_filename)
        self.set_deck(NaipesDeck())

    def play(self):
        self.deck.shuffle()
        self.deal_hands()
        virada = self.deck.draw(1)[0]
        extra_message = f'La carta virada es: {virada}'
        self.notify_players(extra_message)

