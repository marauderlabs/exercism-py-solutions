from functools import reduce
from typing import Dict

def score(word: str) -> int:
    s = 0
    for c in word:
        s += values.get(c.upper(), 0)
    return s

def setup_score_table() -> Dict[chr, int]:
    # Lazy to init the values from the problem. Hence populating it like this.
    _values = {
                "A, E, I, O, U, L, N, R, S, T": 1,
                "D, G": 2,
                "B, C, M, P": 3,
                "F, H, V, W, Y": 4,
                "K" : 5,
                "J,X": 8,
                "Q, Z": 10
               }

    values = {}
    # A value dict - A value for each alphabet
    for letters, value in _values.items():
        for letter in letters.split(','):
            values[letter.strip()] = value
    return values

    for letters, value in _values.items():
        for letter in letters.split(','):
            values[letter.strip()] = value
    return values

# A dict of alphabet to value
values = setup_score_table()
