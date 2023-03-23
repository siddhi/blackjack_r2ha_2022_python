from blackjack_r2ha_2022_python.hand import Hand
from blackjack_r2ha_2022_python.suit import Suit
from blackjack_r2ha_2022_python.rank import Rank
from blackjack_r2ha_2022_python.card import Card


DUMMY_SUIT = Suit.CLUBS


def create_hand(*ranks):
    return Hand(Card(suit=DUMMY_SUIT, rank=rank) for rank in ranks)


def test_hand_with_1_ace_and_other_card_valued_less_than_10_then_ace_is_valued_at_11():
    hand = create_hand(Rank.ACE, Rank.FIVE)

    assert hand.value == 11 + 5


def test_hand_with_one_ace_and_other_cards_valued_at_10_then_ace_is_valued_at_11():
    hand = create_hand(Rank.ACE, Rank.TEN)

    assert hand.value == 11 + 10


def test_hand_with_one_ace_and_other_cards_valued_as_11_then_ace_is_valued_at_1():
    hand = create_hand(Rank.ACE, Rank.EIGHT, Rank.THREE)

    assert hand.value == 1 + 8 + 3
