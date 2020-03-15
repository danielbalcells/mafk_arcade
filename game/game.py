import csv

from player import Player
from mailer import Mailer
from hand import Hand


class BaseGame(object):

    def __init__(self, players_filename):
        self.players = self.load_players(players_filename)
        self.mailer = Mailer(subject=self.game_name)

    def load_players(self, filename):
        with open(filename) as f:
            reader = csv.DictReader(f)
            players = []
            for row in reader:
                players.append(Player(row['name'], row['email']))
        self.n_players = len(players)
        return players

    def set_deck(self, deck):
        self.deck = deck

    def deal_hands(self):
        for player in self.players:
            hand = Hand(self.deck.draw(self.cards_per_hand))
            player.set_hand(hand)

    def notify_players(self, extra_message=''):
        for player in self.players:
            player.notify(self.mailer, extra_message)
