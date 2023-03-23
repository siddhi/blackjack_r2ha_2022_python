from blackjack_r2ha_2022_python.card import Card
from blackjack_r2ha_2022_python.suit import Suit
from blackjack_r2ha_2022_python.rank import Rank
from blackjack_r2ha_2022_python.ansi import Ansi, Colour


DUMMY_SUIT = Suit.HEARTS
DUMMY_RANK = Rank.TEN


def test_number_cards_have_numeric_value_of_number():
    card = Card(suit=DUMMY_SUIT, rank=Rank.SEVEN)
    assert card.rank_value == 7


def test_queen_has_value_ten():
    card = Card(suit=DUMMY_SUIT, rank=Rank.QUEEN)
    assert card.rank_value == 10


def test_ace_has_value_one():
    card = Card(suit=DUMMY_SUIT, rank=Rank.ACE)
    assert card.rank_value == 1


def test_suit_of_hearts_or_diamonds_is_displayed_in_red():
    hearts_card = Card(Suit.HEARTS, DUMMY_RANK)
    diamonds_card = Card(Suit.DIAMONDS, DUMMY_RANK)

    ansi_red_string = str(Ansi().fg(Colour.RED))

    assert ansi_red_string in hearts_card.display()
    assert ansi_red_string in diamonds_card.display()
