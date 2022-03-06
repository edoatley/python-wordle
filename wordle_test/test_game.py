#!/usr/bin/env python3
import unittest
import pathlib
import os
from wordle_main.game import Game
from wordle_main.attempt import Attempt


class TestGame(unittest.TestCase):
    """
    Tests for Game Class
    """

    def test_init_success(self):
        g = Game(self.test_dict())
        self.assertEqual(g.attempt_number, 0)
        self.assertEqual(len(g.attempts), 0)
        self.assertIn(g.current_solution, ["brown", "climb", "drown", "frame"])

    def test_simple_game(self):
        g = Game(self.test_dict())
        g.current_solution = "brown"  # force word to a known value
        g.process_new_attempt("brown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt("brown", "brown"), g.attempts)
        self.assertEqual(g.result, True)

    def test_dict(self):
        current_dir = pathlib.Path().resolve()
        return os.path.join(current_dir, "wordle_test/resources/test-dictionary.txt")


if __name__ == "__main__":
    unittest.main()
