from itertools import count

class Attempt:
    """
    This class represents an attempt at guessing the word the game has selected
    and analyses matches

    The attributes are:
    - word
    - attempt
    """

    # right letter right place
    RLRP = "R"
    # wrong letter wrong place
    WLWP = "W"
    # right letter wrong place
    RLWP = "L"

    def __init__(self, word, attempt):
        self.word = Attempt.validate_input(word, "Word")
        self.attempt = Attempt.validate_input(attempt, "Attempt")
        
    def evaluate(self):
        if self.word == self.attempt:
            return 5 * self.RLRP

        result = ""

        for i in self.word:
            if self.attempt == self.word:
                result = result + self.RLRP
            elif i in self.word:
                if self.word.count(i) == self.attempt.count(i):
                    result = result + self.RLWP
                else:
                    pass  # need to implement a rule that decides whether to give RLWP OR WLWP
            else:
                result = result + self.WLWP
                
    def validate_input(string, label):
        if len(string) != 5:
            raise ValueError(f"{label} {string} is incorrect length")
        elif not string.isalpha():
            raise ValueError(f"{label} {string} is not alpha")
        elif not string == string.lower():
            raise ValueError(f"{label} {string} is not lower case")
        else:
            return string