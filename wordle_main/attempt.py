
class Attempt:
    """
    This class represents an attempt at guessing the word the game has selected
    and analyses matches
    
    The attributes are:
    - word
    - attempt
    """
    
    # right letter right place
    RLRP = 'R'
    # wrong letter wrong place
    WLWP = 'W'
    # right letter wrong place
    RLWP = 'W'
    
    def __init__(self, word, attempt):
        self.word = Attempt.validate_input(word, "Word")
        self.attempt = Attempt.validate_input(attempt, "Attempt")
        
    def evaluate(self):
        if self.word == self.attempt:
            return 5 * self.RLRP
        
        result = 5 * self.WLWP
        
        for i in self.word:
            pass
        
    def validate_input(string, label):
        if len(string) != 5:
            raise ValueError(f'{label} {string} is incorrect length')
        elif not string.isalpha(): 
            raise ValueError(f'{label} {string} is not alpha')
        elif not string == string.lower(): 
            raise ValueError(f'{label} {string} is not lower case')
        else:
            return string