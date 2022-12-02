import unittest
from src.Board import *


class UnittestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_instance_of_board(self):
        self.assertIsInstance(Board(), Board, "Boards should be of instance Board.")
