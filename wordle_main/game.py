from wordle_main.dictionary import Dictionary
from wordle_main.attempt import Attempt


class Game:
    """
    This class represents the overall wordle hame

    The attributes are:
    - attempts []
    - dictionary
    - current_attempt
    """

    def __init__(self):
        self.attempts = [Attempt() for _ in range(6)]
        self.dictionary = Dictionary()
        self.new_game(self)

    def new_game(self):
        self.current_solution = self.dictionary.randomWord()
        self.current_attempt = 0

    def process_new_attempt(self, word: str):
        pass
