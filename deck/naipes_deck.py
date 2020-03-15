from .deck import BaseDeck


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
