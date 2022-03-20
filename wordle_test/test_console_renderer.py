import io
import sys

# def foo(inStr):
#     print ("hi"+inStr)

# def test_foo():
#     capturedOutput = io.StringIO()                  # Create StringIO object
#     sys.stdout = capturedOutput                     #  and redirect stdout.
#     foo('test')                                     # Call function.
#     sys.stdout = sys.__stdout__                     # Reset redirect.
#     print ('Captured', capturedOutput.getvalue())   # Now works as before.

# test_foo()

#!/usr/bin/env python3

import unittest

from attempt import Attempt
from console_renderer import ConsoleRenderer, Colours


class TestConsolerRenderer(unittest.TestCase):
    """
    Tests for ConsoleRenderer Class
    """

    def test_simple_print_one_attempt(self):
        attempts = [Attempt("train", "train")]

        expected = f"{Colours.OKGREEN}T{Colours.ENDC} {Colours.OKGREEN}R{Colours.ENDC} {Colours.OKGREEN}A{Colours.ENDC} {Colours.OKGREEN}I{Colours.ENDC} {Colours.OKGREEN}N{Colours.ENDC}"
        renderer = ConsoleRenderer()
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        renderer.draw_attempts_so_far(attempts)  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        print(expected)
        print(capturedOutput.getvalue())
        self.assertEqual(expected, capturedOutput.getvalue())


if __name__ == "__main__":
    unittest.main()
