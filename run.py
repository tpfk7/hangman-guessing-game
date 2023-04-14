import os
import random
import colorama
from colorama import Fore, Back
from gallows import GALLOWS as gallows
from words import WORDS as mystery_words
colorama.init(autoreset=True)


def intro():
    """
    Function to allow user to start game or read instructions.
    """
    while True:
        print(Fore.GREEN + "Welcome to Hangman!\n")
        user_input = input(
            Fore.YELLOW + "Press 1 to start game, 2 for instructions: "
        )
        if user_input == '1':
            start_game()
            break
        elif user_input == '2':
            instructions()
            break
        else:
            clear()
            print(
                Fore.RED + "Please enter a valid input. "
                f"{user_input} is not valid"
            )


def instructions():
    """
    Function to explain to user how play game and how to start game.
    """
    clear()
    print(
        Fore.YELLOW + "Try and guess the word one letter at a time."
    )
    print(
        Fore.YELLOW + "Every mistake will add an extra "
    )
    print(
        Fore.YELLOW + "piece of the man to the gallows."
    )
    print("")
    while True:
        user_input = input(Fore.BLUE + "Press 1 to start game: ")
        if user_input == '1':
            start_game()
            break
        else:
            clear()
            print(
                Fore.RED + "Please enter a valid input. "
                f"{user_input} is not valid"
            )


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


mystery_word = ""


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
        print(Fore.RED + f"\n{guess} is not valid. Please enter a letter.")
        return False
    return True


def start_game():
    """
    Function to run the game until the user has won or lost.
    """
    clear()
    wrong_guesses = []
    print(Fore.WHITE + gallows[len(wrong_guesses)])
    mystery_word = get_mystery_word()
    partial_solution = "_" * len(mystery_word)
    while len(wrong_guesses) < len(gallows) - 1 and partial_solution != mystery_word:  # noqa
        while True:
            guess = input("Your guess: ").upper()
            if validate_letter(guess):
                for i, x in enumerate(mystery_word):
                    if x == guess:
                        partial_solution = partial_solution[:i] + guess + partial_solution[i+1:]  # noqa
                break
        clear()
        if guess not in mystery_word and guess not in wrong_guesses:
            wrong_guesses.append(guess)
        print(Fore.WHITE + gallows[len(wrong_guesses)])
        print(
            Fore.BLUE + f"Word: {partial_solution}, "
        )
        print(
            Fore.RED + f"Wrong guesses: {','.join(wrong_guesses)}"
        )

    if mystery_word == partial_solution:
        print(Fore.GREEN + "You have won.")
    else:
        print(Fore.RED + f"You have lost. The word was: {mystery_word}")
    print("")
    intro()


if __name__ == "__main__":
    clear()
    intro()
