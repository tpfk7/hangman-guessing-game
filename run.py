import os
import random
from data import GALLOWS as gallows


def intro():
    """
    Function to allow user to start game or read instructions.
    """
    while True:
        user_input = input("Press 1 to start game, 2 for instructions: ")
        if user_input == '1':
            start_game()
            break
        elif user_input == '2':
            instructions()
            break
        else:
            clear()
            print(f"Please enter a valid input. {user_input} is not valid")


def instructions():
    """
    Function to explain to user how play game and how to start game.
    """
    clear()
    print("Try and guess the word one letter at a time.")
    print("Every mistake will add an extra piece of the man to the gallows.")
    while True:
        user_input = input("Press 1 to start game: ")
        if user_input == '1':
            start_game()
            break
        else:
            clear()
            print(f"Please enter a valid input. {user_input} is not valid")


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


mystery_words = [
    "TIGER", "SHARK", "LION", "CHAIR", "BEACH", "HOUSE",
    "BIRD", "WEATHER", "WINDOW", "APPLE", "ORANGE", "HORSE",
    "CARDS", "CASTLE", "TRUCK"
]
mystery_word = ""
wrong_guesses = []


def get_mystery_word():
    """
    Function to choose a random mystery word.
    """
    mystery_word = random.choice(mystery_words)
    return mystery_word


def validate_letter(guess):
    """
    Function to ensure user enters a valide input.
    """
    if not guess.isalpha() or len(guess) != 1:
        print(f"\n{guess} is not valid. Please enter a letter.")
        guess = input("Your guess: ").upper()
        validate_letter(guess)
        return False
    return True


def start_game():
    """
    Function to run the game until the user has won or lost.
    """
    clear()
    wrong_guesses = []
    print(gallows[len(wrong_guesses)])
    mystery_word = get_mystery_word()
    partial_solution = "_" * len(mystery_word)
    while len(wrong_guesses) < len(gallows) - 1 and partial_solution != mystery_word:  # noqa
        print(mystery_word)  # TODO: test only
        # print(f"Word: {partial_solution}")
        guess = input("Your guess: ").upper()
        if validate_letter(guess):
            for i, x in enumerate(mystery_word):
                if x == guess:
                    partial_solution = partial_solution[:i] + guess + partial_solution[i+1:]  # noqa
        clear()
        if guess not in mystery_word and guess not in wrong_guesses:
            wrong_guesses.append(guess)
        print(gallows[len(wrong_guesses)])
        print(
            f"Word: {partial_solution}, "
            f"Wrong guesses: {','.join(wrong_guesses)}"
        )

    if mystery_word == partial_solution:
        print("You have won.")
    else:
        print(f"You have lost. The word was: {mystery_word}")
    print("")
    intro()


if __name__ == "__main__":
    clear()
    intro()
