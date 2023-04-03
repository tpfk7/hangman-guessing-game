import data
import random

mystery_words = ["TIGER","SHARK","LION"]
mystery_word = random.choice(mystery_words)

wrong_guesses = []
partial_solution = "_" * len(mystery_word)
print(mystery_word)

print(data.gallows[len(wrong_guesses)])
print(f"Word: {partial_solution}")
