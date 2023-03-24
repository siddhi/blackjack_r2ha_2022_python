from typing import Iterable, Optional
from .card import Card
from .deck import Deck
from .ansi import Ansi, Colour
from .console import display_card


class Hand:
    def __init__(self, cards: Optional[Iterable[Card]] = None):
        self.cards: list[Card] = list(cards) if cards else []

    @property
    def value(self):
        hand_value = sum(card.rank_value for card in self.cards)

        # does the hand contain at leastt 1 Ace?
        has_ace = any(card.rank_value == 1 for card in self.cards)

        # if the total hand value <= 11, then count the ace as 11 by adding 10
        if has_ace and hand_value <= 11:
            hand_value += 10

        return hand_value

    def display_face_up_card(self):
        return display_card(self.cards[0])

    @property
    def dealer_must_draw_card(self):
        return self.value <= 16

    def display(self):
        print(str(Ansi().cursor_up(6).cursor_right(1)).join(display_card(card) for card in self.cards) + str(Ansi().fg(Colour.BLACK)))

    def draw_from(self, deck: Deck):
        self.cards.append(deck.draw())

    @property
    def is_busted(self):
        return self.value > 21

    def pushes(self, hand: "Hand"):
        return hand.value == self.value

    def beats(self, hand: "Hand"):
        return hand.value < self.value
