#!/usr/bin/env python3
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
        self.assertEqual(test_attempt.result, 5 * "R")

    def test_evaluate_total_mismatch(self):
        test_attempt = Attempt("brown", "sacks")
        self.assertEqual(test_attempt.result, 5 * "W")

    def test_evaluate_single_mismatch(self):
        test_attempt = Attempt("mount", "count")
        self.assertEqual(test_attempt.result, "WRRRR")

    def test_evaluate_double_mismatch(self):
        test_attempt = Attempt("mound", "count")
        self.assertEqual(test_attempt.result, "WRRRW")

    def test_evaluate_triple_mismatch(self):
        test_attempt = Attempt("mould", "count")
        self.assertEqual(test_attempt.result, "WRRWW")

    def test_evaluate_quad_mismatch(self):
        test_attempt = Attempt("mowld", "count")
        self.assertEqual(test_attempt.result, "WRWWW")

    def test_evaluate_quin_mismatch(self):
        test_attempt = Attempt("mawld", "count")
        self.assertEqual(test_attempt.result, "WWWWW")

    def test_evaluate_right_letters_backwards(self):
        test_attempt = Attempt("tnuoc", "count")
        self.assertEqual(test_attempt.result, "LLRLL")

    def test_evaluate_right_letters_wrong_places(self):
        test_attempt = Attempt("tunco", "count")
        self.assertEqual(test_attempt.result, "LLLLL")

    def test_evaluate_duplicate_letter_both_right(self):
        test_attempt = Attempt("tunct", "txxxt")
        self.assertEqual(test_attempt.result, "RWWWR")

    def test_evaluate_duplicate_letter_one_right_one_wrong_place(self):
        test_attempt = Attempt("tunct", "txxtx")
        self.assertEqual(test_attempt.result, "RWWLW")

    def test_multi_match_speed_abide(self):
        test_attempt = Attempt("abide", "speed")
        self.assertEqual(test_attempt.result, "WWLWL")

    def test_multi_match_speed_erase(self):
        test_attempt = Attempt("erase", "speed")
        self.assertEqual(test_attempt.result, "LWLLW")

    def test_multi_match_speed_steal(self):
        test_attempt = Attempt("steal", "speed")
        self.assertEqual(test_attempt.result, "RWRWW")

    def test_multi_match_speed_crepe(self):
        test_attempt = Attempt("crepe", "speed")
        self.assertEqual(test_attempt.result, "WLRLW")


if __name__ == "__main__":
    unittest.main()
