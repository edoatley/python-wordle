from wordle_main.dictionary import Dictionary
from wordle_main.attempt import Attempt
from wordle_main.exceptions import DictionaryError

MAX_ATTEMPTS = 6


class Game:
    """
    This class represents the overall wordle hame

    The attributes are:
    - attempts []
    - dictionary
    - attempt_number
    - result
    """

    def __init__(self, dictionary):
        self.attempts = []
        self.dictionary = Dictionary()
        self.dictionary.load(dictionary)
        self.result = None
        self.new_game()

    def new_game(self):
        self.current_solution = self.dictionary.random_word()
        self.attempt_number = 0

    def process_new_attempt(self, guess: str):
        if not self.dictionary.lookup(guess):
            raise DictionaryError(f"Word {guess} is not in the dictionary")

        attempt = Attempt(self.current_solution, guess)
        attempt.evaluate()
        self.attempts.append(attempt)
        self.attempt_number += 1
        self.check_result()

    def check_result(self):
        if self.attempts[-1].result == 5 * Attempt.RLRP:
            self.result = True
        elif self.attempt_number >= MAX_ATTEMPTS:
            self.result = False
