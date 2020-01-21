from functools import reduce
from typing import Dict

def score(word: str) -> int:
    return sum(values.get(c.upper(), 0) for c in word)

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

    return { letter.strip(): value for letters, value in _values.items() for letter in letters.split(',') }

# A dict of alphabet to value
values = setup_score_table()