import csv
import smtplib
import random


PLAYERS_FILENAME = 'players.csv'


CARDS_PER_HAND = 3


SUITS = [
    'Oros',
    'Copas',
    'Espadas',
    'Bastos',
]


NUMBERS = [
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


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465 
EMAIL_FROMADDR = 'dbalcells@gmail.com'
EMAIL_PASSWORD = 'password'
EMAIL_SUBJECT = 'Envite'


def init_server():
    server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    server.ehlo()
    server.login(EMAIL_FROMADDR, EMAIL_PASSWORD)
    return server


def create_deck():
    return [f'{number} de {suit}' for number in NUMBERS for suit in SUITS]


def shuffle(deck):
    return random.sample(deck, len(deck))


def draw(deck, n_cards=1):
    result = []
    for i in range(n_cards):
        result.append(deck.pop(0))
    return result


def load_players(filename=PLAYERS_FILENAME):
    players = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)


def send_email(player, virada, server):
    body = f"Subject: {EMAIL_SUBJECT}\n"
    body += f"\nHola {player['name']}, tu mano es:\n"
    for card in player['hand']:
        body += f"{card}\n"
    body += f"La carta virada es: {virada}."
    server.sendmail(EMAIL_FROMADDR, player['email'], body)

    
def envite():
    players = load_players()
    deck = create_deck()
    deck = shuffle(deck)
    for player in players:
        hand = draw(deck, CARDS_PER_HAND)
        player['hand'] = hand
    virada = draw(deck, 1)[0]
    server = init_server()
    for player in players:
        send_email(player, virada, server)


if __name__ == '__main__':
    envite()
