class DictionaryError(BaseException):
    """
    Raised when the dictionary rule is not satisfied
    Attributes:
        message: error message
    """

    def __init__(self, message):
        self.message = message


class StateError(BaseException):
    """
    Raised when the game is in an unexpected state
    """

    def __init__(self, message):
        self.message = message
