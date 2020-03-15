class Hand(object):

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return f'<Hand: {self}>'

    def __str__(self):
        return '\n'.join(self.cards)
