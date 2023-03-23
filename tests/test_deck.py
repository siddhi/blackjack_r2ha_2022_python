import pytest
from blackjack_r2ha_2022_python.deck import Deck


@pytest.fixture
def deck():
    return Deck()


def test_full_deck_has_52_cards(deck):
    assert deck.size == 52


def test_draw_card_from_deck_reduces_deck_size_by_one(deck):
    deck.draw()

    assert deck.size == 51


def test_draw_card_from_deck_returns_valid_card(deck):
    card = deck.draw()

    assert card is not None
    assert card.rank_value > 0


def test_draw_all_cards_results_in_52_unique_cards(deck):
    drawn_cards = set()
    for _ in range(52):
        drawn_cards.add(deck.draw())

    assert len(drawn_cards) == 52
