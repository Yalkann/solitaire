import unittest
from src.Deck import *


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.d = Deck()

    def tearDown(self):
        self.d.__init__()

    def test_is_instance_of_deck(self):
        self.assertIsInstance(self.d, Deck, "Decks should an instance of Deck.")

    def test_is_deck_shuffled(self):
        decks = {}
        nbd = 10
        for i in range(nbd):
            d = Deck()
            d.shuffle()
            decks[str(d.getDeck())] = i
        self.assertEqual(len(decks), nbd, "Decks should be different when shuffled.")

    def test_contains_no_illegal_cards(self):
        for card in self.d.getDeck():
            c = card.getCard()
            self.assertTrue(
                c[0] >= 1 and c[0] <= 13 and c[1] in SUITS,
                "Decks should contain no illegal cards.",
            )

    def test_deck_is_of_correct_size(self):
        self.assertEqual(
            self.d.getDeckLen(),
            52,
            "Decks should have the correct amount of cards on creation.",
        )

    def test_removing_cards_from_deck(self):
        for i in range(1, 53):
            self.d.removeTopCard()
            self.assertEqual(
                self.d.getDeckLen(),
                52 - i,
                "Deck size should lower by one when removing a card.",
            )

    def test_is_empty_after_removing_all_cards(self):
        for _ in range(52):
            self.assertFalse(
                self.d.isEmpty(),
                "Decks should not be empty before removing every cards.",
            )
            self.d.removeTopCard()
        self.assertTrue(
            self.d.isEmpty(), "Decks should be empty after removing every cards."
        )

    def test_cannot_remove_card_from_empty_deck(self):
        for _ in range(52):
            self.d.removeTopCard()
        with self.assertRaises(Exception):
            self.d.removeTopCard(), "Should not be able to remove a card from an empty deck."

    def test_removed_card_is_the_correct_one(self):
        card = self.d.getTopCard()
        self.d.removeTopCard()
        self.assertFalse(
            card in self.d.getDeck(),
            "A removed card should not be present in the deck.",
        )

    def test_card_sent_to_back_of_deck(self):
        card = self.d.getTopCard()
        self.d.removeTopCard()
        self.d.sendToBack(card)
        for _ in range(51):
            self.d.removeTopCard()
        self.assertEqual(
            card,
            self.d.getTopCard(),
            "Cards are not properly sent to the back of the deck.",
        )

    def test_cannot_send_duplicate_to_back_of_deck(self):
        card = self.d.getTopCard()
        with self.assertRaises(Exception):
            self.d.sendToBack(
                card
            ), "Should not be able to send duplicate cards to the back of the deck."
