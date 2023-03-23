from enum import Enum


class Suit(Enum):
    HEARTS = ("♥", True)
    CLUBS = ("♣", False)
    DIAMONDS = ("♦", True)
    SPADES = ("♠", False)

    @property
    def symbol(self):
        return self.value[0]

    @property
    def is_red(self):
        return self.value[1]
