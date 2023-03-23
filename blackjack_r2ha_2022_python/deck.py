from itertools import product
import random
from .suit import Suit
from .rank import Rank
from .card import Card


class Deck:
    def __init__(self):
        all_cards = product(Suit, Rank)
        self.cards = [Card(suit, rank) for suit, rank in all_cards]
        random.shuffle(self.cards)

    @property
    def size(self):
        return len(self.cards)

    def draw(self):
        return self.cards.pop()
