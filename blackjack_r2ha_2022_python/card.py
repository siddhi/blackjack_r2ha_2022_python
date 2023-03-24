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

    def display(self):
        d = str(self.get_rank().display)  
        p = "" if self.get_rank() == Rank.TEN else " "
        s = self.get_suit().symbol
        card_colour = Colour.RED if self.get_suit().is_red else Colour.BLACK
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
