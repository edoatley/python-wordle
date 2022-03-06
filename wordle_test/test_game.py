#!/usr/bin/env python3
import unittest
import pathlib
import os
from game import Game

class TestGame(unittest.TestCase):
    """
    Tests for Game Class
    """
    
    def test_init_success(self):
        g = Game(self.test_dict())
        self.assertEqual(g.current_attempt, 0)
        self.assertEqual(len(g.attempts), 0)
        self.assertIn(g.current_solution, ["brown", "climb", "drown", "frame"])

    def test_dict(self):
        current_dir = pathlib.Path().resolve()
        return os.path.join(current_dir, 'wordle_test/resources/test-dictionary.txt')  

if __name__ == "__main__":
    unittest.main()
