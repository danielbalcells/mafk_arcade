import argparse

from game.politico import Politico
from game.insider import Insider
from game.envite import Envite


OPT_POLITICO = 'politico'
OPT_INSIDER = 'insider'
OPT_ENVITE = 'envite'


CHOICES = {
    OPT_POLITICO: Politico,
    OPT_INSIDER: Insider,
    OPT_ENVITE: Envite,
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='mafk_arcade.py')
    parser.add_argument('--game', choices=CHOICES.keys())
    parser.add_argument('--players', type=str, default='players.csv')
    args = parser.parse_args()

    game_cls = CHOICES[args.game]
    game = game_cls(args.players)
    game.play()
