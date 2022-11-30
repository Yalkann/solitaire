import unittest
from src.Card import *


class TestStack(unittest.TestCase):
    def setUp(self):
        self.correctCard = Card(2, "Spades")
        self.incorrectCard1 = Card(0, "Spades")
        self.incorrectCard2 = Card(2, "Inorrect_suite")
        self.incorrectCard3 = Card(0, "Incorrect_suite")
        self.cards = [
            self.correctCard,
            self.incorrectCard1,
            self.incorrectCard2,
            self.incorrectCard3,
        ]

    def test_is_instance_of_card(self):
        for card in self.cards:
            self.assertIsInstance(card, Card, "cards should be of instance Card.")
