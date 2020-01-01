from typing import List

gifts = [
    "and a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]

days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

def make_verse(day: int) -> str:
    first = f"On the {days[day]} day of Christmas my true love gave to me: "
    rest = ", ".join(reversed(gifts[:day+1]))
    out = first + rest
    if day == 0:
        out = out.replace('and ', '')
    return out


def recite(start_verse: int, end_verse: int) -> List[str]:
    return [make_verse(i) for i in range(start_verse-1, end_verse)]
