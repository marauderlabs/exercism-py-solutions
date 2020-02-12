import itertools
from typing import List
from collections import Counter

# An iota (gives the next enum value) like the iota in golang
_counter = itertools.count()
iota = lambda: next(_counter)

# Score categories.
YACHT = iota()
ONES = iota()
TWOS = iota()
THREES = iota()
FOURS = iota()
FIVES = iota()
SIXES = iota()
FULL_HOUSE = iota()
FOUR_OF_A_KIND = iota()
LITTLE_STRAIGHT = iota()
BIG_STRAIGHT = iota()
CHOICE = iota()

# Handlers for different categories. The ones that might not look good as
# lambdas are defined here.

def four_of_a_kind(dice: List[int]) -> int:
    for k, v in Counter(dice).items():
        if v >= 4:
            return 4*k
    return 0

handlers = {
            YACHT: lambda dice: 50 if len(set(dice)) == 1 else 0,
            ONES: lambda dice: dice.count(1),
            TWOS: lambda dice: 2 * dice.count(2),
            THREES: lambda dice: 3 * dice.count(3),
            FOURS: lambda dice: 4 * dice.count(4),
            FIVES: lambda dice: 5 * dice.count(5),
            SIXES: lambda dice: 6 * dice.count(6),
            FULL_HOUSE: lambda dice: sum(dice) if [2, 3] == sorted(list(Counter(dice).values())) else 0,
            FOUR_OF_A_KIND: four_of_a_kind,
            LITTLE_STRAIGHT: lambda dice: 30 if sorted(dice) == list(range(1, 6)) else 0,
            BIG_STRAIGHT: lambda dice: 30 if sorted(dice) == list(range(2, 7)) else 0,
            CHOICE: lambda dice: sum(dice),
        }

def score(dice, category):
    if len(dice) != 5:
        raise ValueError("Invalid dice rolls")
    return handlers[category](dice)
