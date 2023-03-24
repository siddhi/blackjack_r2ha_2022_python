from dataclasses import dataclass
from .suit import Suit
from .rank import Rank


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    @property
    def rank_value(self):
        return self.rank.points
