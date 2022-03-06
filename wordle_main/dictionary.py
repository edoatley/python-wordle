from random import randrange
import os

class Dictionary:
    """
    This class represents the dictionary wordle uses to check word validity
    or provide a random word

    The attributes are:
    - words []
    """

    def __init__(self, words=[]):
        self.words = words

    def load(self, dictionary_location: str = "wordle.conf"):
        try:
            with open(dictionary_location, "r") as dict:
                for word in dict:
                    self.words.append(word.rstrip("\n"))
        except FileNotFoundError:
            print(f"Unable to find dictionary file {dictionary_location}")
            raise

    def size(self):
        return len(self.words)

    def random_word(self):
        return self.words[randrange(0, len(self.words))]

    def lookup(self, candidate):
        if len(candidate) == 5:
            return candidate in self.words
        return False