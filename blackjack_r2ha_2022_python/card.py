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

    def display(self):
        d = str(self.rank.display)
        p = "" if self.rank == Rank.TEN else " "
        s = self.suit.symbol
        card_colour = Colour.RED if self.suit.is_red else Colour.BLACK
        lines = [
            "┌─────────┐",
            f"│{d}{p}       │",
            "│         │",
            f"│    {s}    │",
            "│         │",
            f"│       {p}{d}│",
            "└─────────┘",
        ]
        return str(Ansi().fg(card_colour)) + str(
            Ansi().cursor_down(1).cursor_left(11)
        ).join(lines)
