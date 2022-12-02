import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from UnittestCard import *
from UnittestDeck import *
from UnittestStack import *


if __name__ == "__main__":
    # Card Tests
    unittestCard = UnittestCard()

    # Deck Tests
    unittestDeck = UnittestDeck()

    # Stack Tests
    unittestStack = UnittestStack()

    unittest.main()
