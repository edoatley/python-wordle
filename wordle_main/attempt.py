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
        self.result = self.evaluate()

    def evaluate(self):
        if self.word == self.attempt:
            return 5 * self.RLRP

        r = ""

        for (i, c) in enumerate(self.attempt):
            if self.word[i] == c:
                r = r + self.RLRP
            elif c not in self.word:
                r = r + self.WLWP
            else:
                count_in_word = self.word.count(c)
                count_in_attempt = self.attempt.count(c)
                count_sofar_in_attempt = self.attempt[:i].count(c)
                count_sofar_in_word = self.word[:i].count(c)
                if (
                    count_in_word == count_in_attempt
                    or count_sofar_in_attempt < count_in_word
                ):
                    r = r + self.RLWP
                else:
                    r = r + self.WLWP

        return r

    def validate_input(string, label):
        if len(string) != 5:
            raise ValueError(f"{label} {string} is incorrect length")
        elif not string.isalpha():
            raise ValueError(f"{label} {string} is not alpha")
        elif not string == string.lower():
            raise ValueError(f"{label} {string} is not lower case")
        else:
            return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Attempt):
            return self.attempt == other.attempt
        return False
