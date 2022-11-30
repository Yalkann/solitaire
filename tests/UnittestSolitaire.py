import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from TestDeck import *
from TestStack import *


if __name__ == "__main__":

    # Deck Tests
    deckTest = TestDeck()

    # Stack Tests
    stackTest = TestStack()

    unittest.main()
