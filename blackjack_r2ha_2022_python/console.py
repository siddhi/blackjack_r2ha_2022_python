from .rank import Rank
from .ansi import Ansi, Colour

def display_card(card):
    d = str(card.get_rank().display)  
    p = "" if card.get_rank() == Rank.TEN else " "
    s = card.get_suit().symbol
    card_colour = Colour.RED if card.get_suit().is_red else Colour.BLACK
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
