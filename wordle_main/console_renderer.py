from attempt import Attempt
from colours import Colours


class ConsoleRenderer:
    def obtain_guess(self):
        guess = input("what is your next guess?")
        return guess

    def draw_attempts_so_far(self, attempts):
        for a in attempts:
            self.print_attempt(a)

    def print_attempt(self, attempt):
        letters = []
        for i in range(len(attempt.attempt)):
            letter = attempt.attempt[i].upper()
            if attempt.result[i] == Attempt.RLRP:
                letters.append(f"{Colours.GREEN}{letter}{Colours.ENDC}")
            elif attempt.result[i] == Attempt.RLWP:
                letters.append(f"{Colours.YELLOW}{letter}{Colours.ENDC}")
            elif attempt.result[i] == Attempt.WLWP:
                letters.append(f"{Colours.RED}{letter}{Colours.ENDC}")
            else:
                raise ValueError("Unknown result:{attempt.result[i]}")

        message = " ".join(letters)
        print(message)

    def warn_user(self, error: Exception):
        print(f"{Colours.RED}{Colours.BOLD}{error.message}{Colours.ENDC}")
