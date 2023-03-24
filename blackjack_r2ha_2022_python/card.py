from dataclasses import dataclass
from .suit import Suit
from .rank import Rank
from .ansi import Ansi, Colour


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    @property
    def rank_value(self):
        return self.rank.points

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

