#!/usr/bin/env python3

import unittest

from wordle_main.dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    """
    Tests for Dictionary Class
    """

    TEST_WORDS_SET_1 = ["adapt", "blame", "brown", "climb", "drown", "frame", "trout"]

    def test_create_nowords(self):
        test_dict = Dictionary()
        self.assertSequenceEqual(test_dict.words, [])

    def test_create_words(self):
        test_dict = Dictionary(self.TEST_WORDS_SET_1)
        self.assertSequenceEqual(test_dict.words, self.TEST_WORDS_SET_1)

    def test_load_success(self):
        test_dict = Dictionary()
        test_dict.load("./wordle_test/resources/test-dictionary.txt")
        self.assertEqual(7, test_dict.size())

    def test_load_failed_no_dictionary(self):
        test_dict = Dictionary()
        # Unittest's assertRaises takes a callable and arguments
        # see https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        self.assertRaises(
            FileNotFoundError, test_dict.load, "./wordle_test/dict-does-not-exist.txt"
        )

    def test_random_word(self):
        test_dict = Dictionary(self.TEST_WORDS_SET_1)
        for i in range(10):
            word = test_dict.random_word()
            self.assertIn(word, self.TEST_WORDS_SET_1)

    def test_lookup_too_big(self):
        test_dict = Dictionary(self.TEST_WORDS_SET_1)
        self.assertFalse(test_dict.lookup("longer"))

    def test_lookup_too_small(self):
        test_dict = Dictionary(self.TEST_WORDS_SET_1)
        self.assertFalse(test_dict.lookup("four"))

    def test_lookup_missing(self):
        test_dict = Dictionary(self.TEST_WORDS_SET_1)
        self.assertFalse(test_dict.lookup("whine"))

    def test_lookup_present(self):
        test_dict = Dictionary(self.TEST_WORDS_SET_1)
        self.assertTrue(test_dict.lookup("adapt"))
        self.assertTrue(test_dict.lookup("blame"))
        self.assertTrue(test_dict.lookup("brown"))
        self.assertTrue(test_dict.lookup("climb"))
        self.assertTrue(test_dict.lookup("drown"))
        self.assertTrue(test_dict.lookup("frame"))
        self.assertTrue(test_dict.lookup("trout"))


if __name__ == "__main__":
    unittest.main()
