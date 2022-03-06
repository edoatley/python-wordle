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

    def test_one_turn_game_immediate_victory(self):
        g = Game(self.test_dict())
        correct_answer = "brown"
        g.current_solution = correct_answer  # force word to a known value

        g.process_new_attempt("brown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt(correct_answer, "brown"), g.attempts)
        self.assertEqual(g.result, True)

    def test_two_turn_game_rapid_victory(self):
        g = Game(self.test_dict())
        correct_answer = "brown"
        g.current_solution = correct_answer  # force word to a known value

        g.process_new_attempt("drown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt(correct_answer, "drown"), g.attempts)

        g.process_new_attempt("brown")
        self.assertEqual(len(g.attempts), 2)
        self.assertIn(Attempt(correct_answer, "brown"), g.attempts)

        self.assertEqual(g.result, True)

    def test_three_turn_game_victory(self):
        g = Game(self.test_dict())
        correct_answer = "brown"
        g.current_solution = correct_answer  # force word to a known value

        g.process_new_attempt("drown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt(correct_answer, "drown"), g.attempts)

        g.process_new_attempt("climb")
        self.assertEqual(len(g.attempts), 2)
        self.assertIn(Attempt(correct_answer, "climb"), g.attempts)

        g.process_new_attempt("brown")
        self.assertEqual(len(g.attempts), 3)
        self.assertIn(Attempt(correct_answer, "brown"), g.attempts)

        self.assertEqual(g.result, True)

    def test_dict(self):
        current_dir = pathlib.Path().resolve()
        return os.path.join(current_dir, "wordle_test/resources/test-dictionary.txt")


if __name__ == "__main__":
    unittest.main()
