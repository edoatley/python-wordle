#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from wordle_main.console_renderer import ConsoleRenderer, Colours
from wordle_main.attempt import Attempt


class TestConsolerRenderer(unittest.TestCase):
    """
    Tests for ConsoleRenderer Class
    """

    @patch('builtins.print')
    def test_simple_print_one_attempt(self, mock_stdout):
        expected = f"{Colours.OKGREEN}T{Colours.ENDC} {Colours.OKGREEN}R{Colours.ENDC} {Colours.OKGREEN}A{Colours.ENDC} {Colours.OKGREEN}I{Colours.ENDC} {Colours.OKGREEN}N{Colours.ENDC}"
        ConsoleRenderer().draw_attempts_so_far([Attempt("train", "train")])
        mock_stdout.assert_called_with(expected)

   
if __name__ == "__main__":
    unittest.main()
