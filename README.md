# mafk_arcade
Dealing with coronavirus.

Deals hands for a number of card games, and emails them to the players.

# Usage
`python mafk_arcade.py --game [option] --players [players_filename]`

Game options are:
- Envite: `envite`
- Insider: `insider`
- Político: `politico`

The `players` option defaults to `players.csv`.

# Adding games
1. Include a single Python file in `games/`, adding a subclass of `base.BaseGame` where you code the card dealing logic. 
2. Optionally, create a subclass of `base.BaseDeck` if the game requires a non-standard deck.
3. Include the new game in `mafk_arcade.py`.
