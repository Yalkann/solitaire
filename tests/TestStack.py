import unittest
import random as rd
from src.Stack import *


class TestStack(unittest.TestCase):
    def setUp(self):
        self.l = [rd.randint(0, 99) for i in range(100)]
        self.s = Stack(self.l)

    def tearDown(self):
        self.s.__init__(self.l)

    def test_is_instance_of_stack(self):
        self.assertIsInstance(self.s, Stack, "Stacks should be an instance of Stack.")

    def test_get_stack_returns_whole_stack(self):
        self.assertEqual(
            self.l,
            self.s.getStack(0),
            "Stacks should be equal to the list they were created from.",
        )

    def test_get_sub_stack(self):
        id = rd.randint(0, 99)
        self.assertEqual(
            self.l[id::],
            self.s.getStack(id),
            "Sub-stacks should be equal to the original sub-list starting from the same index.",
        )

    def test_get_sub_stack_with_incorrect_index(self):
        with self.assertRaises(IndexError):
            self.s.getStack(
                100
            ), "Index should be greater than or equal to 0 and smaller than the stack's length."
            self.getStack(
                -1
            ), "Index should be greater than or equal to 0 and smaller than the stack's length"

    def test_get_sub_stack_from_empty_stack(self):
        s = Stack([])
        self.assertEqual(s.getStack(0), [])

    def test_remove_from_stack(self):
        id = rd.randint(0, 99)
        self.s.remove(id)
        self.assertEqual(
            self.l[0:id],
            self.s.getStack(0),
            "Sub-stacks should be equal to the original sub-list ending at the same index.",
        )

    def test_remove_from_stack_with_incorrect_index(self):
        with self.assertRaises(IndexError):
            self.s.remove(
                100
            ), "Index should be greater than or equal to 0 and smaller than the stack's length."
            self.remove(
                -1
            ), "Index should be greater than or equal to 0 and smaller than the stack's length"

    def test_remove_from_empty_stack(self):
        s = Stack([])
        with self.assertRaises(Exception):
            s.remove(0)

    def test_is_empty_stack(self):
        self.s.remove(0)
        self.assertTrue(self.s.isEmpty())
