from hand import Hand


class Player(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<Player {self}>'

    def __str__(self):
        return f'{self.name} - {self.email}'

    def set_hand(self, hand):
        self.hand = hand

    def notify(self, mailer, extra_message=''):
        message = f'Hola {self.name}, tu mano es:\n'
        message += f'{self.hand}\n'
        message += extra_message
        mailer.send(self.email, message)
