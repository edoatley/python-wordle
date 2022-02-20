#!/usr/bin/env python3
import sys

print(sys.path)

import unittest

from attempt import Attempt

class TestAttempt(unittest.TestCase):
    """
    Tests for Attempt Class
    """

    def test_init_success(self):
        test_attempt = Attempt("brown", "grown")
        self.assertEqual("brown", test_attempt.word)
        self.assertEqual("grown", test_attempt.attempt)
    def test_validate_input_valid(self):
        self.assertEqual("brown", Attempt.validate_input("brown", "Label"))
    def test_validate_wrong_length(self):
        with self.assertRaises(ValueError) as cm:
            Attempt.validate_input("brownx", "Wrong Length")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Wrong Length brownx is incorrect length")
    def test_validate_not_alpha(self):
        with self.assertRaises(ValueError) as cm:
            Attempt.validate_input("br0wn", "Not Alpha")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Not Alpha br0wn is not alpha")
    def test_validate_not_lower(self):
        with self.assertRaises(ValueError) as cm:
            Attempt.validate_input("brOwn", "Not Lower")
        msg = cm.exception.args[0]
        self.assertEqual(msg, "Not Lower brOwn is not lower case")
    def test_evaluate_exact_match(self):
        test_attempt = Attempt("brown", "brown")
        self.assertEqual(test_attempt.evaluate(), 5 * "R")
    def test_evaluate_total_mismatch(self):
        test_attempt = Attempt("brown", "sacks")
        self.assertEqual(test_attempt.evaluate(), 5 * "W")
    def test_evaluate_single_mismatch(self):
        test_attempt = Attempt("mount", "count")
        self.assertEqual(test_attempt.evaluate(), "WRRRR")

if __name__ == "__main__":
    unittest.main()
