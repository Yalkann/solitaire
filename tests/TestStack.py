import unittest
import random as rd
from src.Stack import *


class TestStack(unittest.TestCase):
    def setUp(self):
        self.l = [rd.randint(0, 99) for _ in range(100)]
        self.s = Stack(self.l)

    def tearDown(self):
        self.s.__init__(self.l)

    def test_is_instance_of_stack(self):
        self.assertIsInstance(self.s, Stack, "Stacks should be an instance of Stack.")

    def test_get_stack_list_returns_whole_stack_list(self):
        self.assertEqual(
            self.l,
            self.s.getList(0),
            "Stack lists should be equal to the list the stack was created from.",
        )

    def test_get_stack_sub_list(self):
        id = rd.randint(0, 99)
        self.assertEqual(
            self.l[id::],
            self.s.getList(id),
            "Stack sub-lists should be equal to the original sub-list starting from the same index.",
        )

    def test_get_stack_sub_list_with_incorrect_index(self):
        with self.assertRaises(IndexError):
            self.s.getList(
                100
            ), "Index should be greater than or equal to 0 and smaller than the stack's length."
            self.getStack(
                -1
            ), "Index should be greater than or equal to 0 and smaller than the stack's length"

    def test_get_stack_sub_list_from_empty_stack(self):
        s = Stack([])
        self.assertEqual(s.getList(0), [], "Should get an empty list")

    def test_remove_from_stack(self):
        id = rd.randint(0, 99)
        self.s.remove(id)
        self.assertEqual(
            self.l[0:id],
            self.s.getList(0),
            "Stack sub-lists should be equal to the original sub-list ending at the same index.",
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
            s.remove(0), "Cannot remove a stack sub-list from an empty stack."

    def test_is_empty_stack(self):
        self.s.remove(0)
        self.assertTrue(self.s.isEmpty(), "Stack should be empty.")
