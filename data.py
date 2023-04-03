"""
Set of characters to display the gallows for the python game.
This code was taken from madeinouweland:
https://github.com/madeinouweland/python-hangman/blob/main/data.py
"""

gallows = r"""
+---
|
|
|
^
+---,
|
|
|
^
+---,
|   o
|
|
^
+---,
|   o
|   |
|
^
+---,
|   o
|  /|
|
^
+---,
|   o
|  /|\
|
^
+---,
|   o
|  /|\
|  /
^
+---,
|   o
|  /|\
|  / \
^
""".strip().split("\n\n")
