import os
import random
from data import GALLOWS as gallows


def intro():
    x = (input("Choose 1 to start, 2 for instructions: "))
    while x != (1,2):
        print("Please enter a valid input")
        break






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

    while len(wrong_guesses) < len(gallows) - 1 and partial_solution != mystery_word:
        print(mystery_word)  # TODO: test only
        print(f"Word: {partial_solution}")
        guess = input("Your guess: ").upper()
        if validate_letter(guess):
            for i, x in enumerate(mystery_word):
                if x == guess:
                    partial_solution = partial_solution[:i] + guess + partial_solution[i+1:]
        clear()
        if guess in mystery_word:
            pass
        else:
            if guess not in wrong_guesses:
                wrong_guesses.append(guess)
        print(gallows[len(wrong_guesses)])
        print(f"Word: {partial_solution}, Wrong guesses: {','.join(wrong_guesses)}")

    if mystery_word == partial_solution:
        print("You have won.")
    else:
        print(f"You have lost. The word was: {mystery_word}")


if __name__ == "__main__":
    clear()
    intro()
    # start_game()
