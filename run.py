import os
import random
from data import GALLOWS as gallows


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


mystery_words = ["TIGER", "SHARK", "LION"]
mystery_word = ""
wrong_guesses = []


def get_mystery_word():
    mystery_word = random.choice(mystery_words)
    return mystery_word


def validate_letter(guess):
    if not guess.isalpha() or len(guess) != 1:
        print(f"\n{guess} is not valid. Please enter a letter.")
        guess = input("Your guess: ").upper()
        validate_letter(guess)
        return False
    return True


def start_game():
    print(gallows[len(wrong_guesses)])
    mystery_word = get_mystery_word()
    partial_solution = "_" * len(mystery_word)

    while len(wrong_guesses) < len(gallows) - 1:
        print(mystery_word)  # TODO: test only
        print(f"Word: {partial_solution}")
        guess = input("Your guess: ").upper()
        if validate_letter(guess):
            pass
        clear()
        if guess in mystery_word:
            pass
        else:
            wrong_guesses.append(guess)
        print(gallows[len(wrong_guesses)])


if __name__ == "__main__":
    clear()
    start_game()
