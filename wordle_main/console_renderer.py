class Colours:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class ConsoleRenderer:
    def obtain_guess(self):
        pass

    def draw_attempts_so_far(self, attempts):
        pass

    def print_attempt(self, attempt):
        letters = []
        for i in range(len(attempt.attempt)):
            if attempt.result[i] == Attempt.RLRP:
                letters.append(f"{Colours.OKGREEN}{attempt.attempt[i]}{Colours.ENDC}")
            elif attempt.result[i] == Attempt.RLWP:
                letters.append(f"{Colours.WARNING}{attempt.attempt[i]}{Colours.ENDC}")
            else:
                letters.append(f"{Colours.FAIL}{attempt.attempt[i]}{Colours.ENDC}")

        message = " ".join(letters)
        print(message)

    def warn_user(self, error: Exception):
        pass
