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

    def __init__(self, dictionary):
        self.attempts = []
        self.dictionary = Dictionary()
        self.dictionary.load(dictionary)
        self.new_game()

    def new_game(self):
        self.current_solution = self.dictionary.random_word()
        self.current_attempt = 0

    def process_new_attempt(self, word: str):
        pass
