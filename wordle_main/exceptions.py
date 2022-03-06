class Error(Exception):
    pass


class DictionaryError(Error):
    """
    Raised when the dictionary rule is not satisfied
    Attributes:
        message: error message
    """

    def __init__(self, message):
        self.message = message
