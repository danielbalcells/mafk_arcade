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


class NaipesDeck(BaseDeck):

    suits = [
        'Oros',
        'Copas',
        'Espadas',
        'Bastos',
    ]

    numbers = [
        'As',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        'Sota',
        'Caballo',
        'Rey',
    ]

    def __init__(self):
        super(NaipesDeck, self).__init__()

    def create_deck(self):
        return [f'{n} de {s}' for n in self.numbers for s in self.suits]
