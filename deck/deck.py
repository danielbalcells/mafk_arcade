import random


class BaseDeck(object):

    def __init__(self):
        self.cards = self.create_deck()

    def shuffle(self):
        return random.shuffle(self.cards)

    def draw(self, n_cards):
        results = []
        for i in range(n_cards):
            results.append(self.cards.pop())
        return results
