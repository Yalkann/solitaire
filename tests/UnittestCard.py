import unittest
from src.Card import *


class UnittestCard(unittest.TestCase):
    def test_is_instance_of_card(self):
        self.assertIsInstance(
            Card(2, "Spades"), Card, "cards should be of instance Card."
        )

    def test_cannot_create_illegal_cards(self):
        with self.assertRaises(Exception):
            Card(2, "Incorrect_Suite"), "Cards suites should be in {}".format(*SUITES)
            Card(0, "Spades"), "Cards values should be in 1-13"

    def test_card_suite_is_correct(self):
        self.assertEquals(
            Card(2, "Spades").getSuite(),
            "Spades",
            "Cards suites should be the same as the suite defined during creation.",
        )

    def test_card_value_is_correct(self):
        self.assertEqual(
            Card(2, "Spades").getValue(),
            2,
            "Cards values should be the same as the value defined during creation.",
        )

    def test_card_is_correct(self):
        self.assertEqual(
            Card(2, "Spades").getCard(),
            (2, "Spades"),
            "Cards values and suites should be the same as those defined during creation.",
        )
