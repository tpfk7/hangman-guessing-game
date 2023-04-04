"""
Set of characters to display the gallows for the python game.
This code was taken from madeinouweland:
https://github.com/madeinouweland/python-hangman/blob/main/data.py
"""

GALLOWS = {
    0: """
    +---
    |
    |
    |
    ^
    """,
    1: """
    +---,
    |
    |
    |
    ^
    """,
    2: """
    +---,
    |   o
    |
    |
    ^
    """,
    3: """
    +---,
    |   o
    |   |
    |
    ^
    """,
    4: """
    +---,
    |   o
    |  /|
    |
    ^
    """,
    5: """
    +---,
    |   o
    |  /|\\
    |
    ^
    """,
    6: """
    +---,
    |   o
    |  /|\\
    |  /
    ^
    """,
    7: """
    +---,
    |   o
    |  /|\\
    |  / \\
    ^
    """
    }
