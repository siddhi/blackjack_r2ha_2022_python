from blackjack_r2ha_2022_python.card import Card
from blackjack_r2ha_2022_python.rank import Rank
from blackjack_r2ha_2022_python.suit import Suit
from blackjack_r2ha_2022_python.console import display_card


def test_display_ten_as_string():
    card = Card(Suit.DIAMONDS, Rank.TEN)
    assert (
        display_card(card)
        == "\x1b[0;31;49m┌─────────┐"
        + "\x1b[1B\x1b[11D│10       │"
        + "\x1b[1B\x1b[11D│         │"
        + "\x1b[1B\x1b[11D│    ♦    │"
        + "\x1b[1B\x1b[11D│         │"
        + "\x1b[1B\x1b[11D│       10│"
        + "\x1b[1B\x1b[11D└─────────┘"
    )


def test_display_non_ten_as_string():
    card = Card(Suit.CLUBS, Rank.ACE)
    assert (
        display_card(card)
        == "\x1b[0;30;49m┌─────────┐"
        + "\x1b[1B\x1b[11D│A        │"
        + "\x1b[1B\x1b[11D│         │"
        + "\x1b[1B\x1b[11D│    ♣    │"
        + "\x1b[1B\x1b[11D│         │"
        + "\x1b[1B\x1b[11D│        A│"
        + "\x1b[1B\x1b[11D└─────────┘"
    )
