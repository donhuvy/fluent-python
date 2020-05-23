import pytest

from french_deck import Card, FrenchDeck

def test_french_deck():
    deck = FrenchDeck()
    assert len(deck) == 52
    assert deck[0] == Card(rank="2", suit="spades")
    aces = deck[12::13]
    for ace in aces:
        assert ace.rank == "A"
    assert Card("Q", "hearts") in deck
    assert Card("1", "diamonds") not in deck
    
   
if __name__ == "__main__":
    pytest.main()
