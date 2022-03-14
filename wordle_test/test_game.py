#!/usr/bin/env python3
import unittest
import pathlib
import os
from wordle_main.game import Game
from wordle_main.attempt import Attempt
from wordle_main.exceptions import StateError, DictionaryError


class TestGame(unittest.TestCase):
    """
    Tests for Game Class
    """

    TEST_WORDS_SET_1 = ["adapt", "blame", "brown", "climb", "drown", "frame", "trout"]

    def test_init_success(self):
        g = Game(self.test_dict())
        self.assertEqual(g.attempt_number, 0)
        self.assertEqual(len(g.attempts), 0)
        self.assertIn(g.current_solution, self.TEST_WORDS_SET_1)

    def test_one_turn_game_immediate_victory(self):
        g, correct_answer = self.set_word_to_brown()

        g.process_new_attempt("brown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt(correct_answer, "brown"), g.attempts)
        self.assertEqual(g.result, True)

    def test_two_turn_game_rapid_victory(self):
        g, correct_answer = self.set_word_to_brown()

        g.process_new_attempt("drown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt(correct_answer, "drown"), g.attempts)

        g.process_new_attempt("brown")
        self.assertEqual(len(g.attempts), 2)
        self.assertIn(Attempt(correct_answer, "brown"), g.attempts)

        self.assertEqual(g.result, True)

    def test_three_turn_game_victory(self):
        g, correct_answer = self.set_word_to_brown()

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

    def test_repeat_attempt_forbidden(self):
        g, correct_answer = self.set_word_to_brown()

        g.process_new_attempt("drown")
        self.assertEqual(len(g.attempts), 1)
        self.assertIn(Attempt(correct_answer, "drown"), g.attempts)

        with self.assertRaises(StateError) as cm:
            g.process_new_attempt("drown")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Guess drown already attempted")

    def test_attempt_after_victory_forbidden(self):
        g, correct_answer = self.set_word_to_brown()
        g.process_new_attempt("brown")

        with self.assertRaises(StateError) as cm:
            g.process_new_attempt("brown")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Game has been completed")

    def test_attempt_after_defeat_forbidden(self):
        g, correct_answer = self.set_word_to_brown()
        g.process_new_attempt("adapt")
        g.process_new_attempt("blame")
        g.process_new_attempt("climb")
        g.process_new_attempt("drown")
        g.process_new_attempt("frame")
        g.process_new_attempt("trout")
        self.assertFalse(g.result)

        with self.assertRaises(StateError) as cm:
            g.process_new_attempt("brown")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Player has lost and making more attempts")

    def test_attempt_invalid_word_forbidden(self):
        g, correct_answer = self.set_word_to_brown()

        with self.assertRaises(DictionaryError) as cm:
            g.process_new_attempt("aaaaa")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Word aaaaa is not in the dictionary")

    def test_dict(self):
        current_dir = pathlib.Path().resolve()
        return os.path.join(current_dir, "wordle_test/resources/test-dictionary.txt")

    # utility method
    def set_word_to_brown(self):
        g = Game(self.test_dict())
        correct_answer = "brown"
        g.current_solution = correct_answer  # force word to a known value
        return g, correct_answer


if __name__ == "__main__":
    unittest.main()
