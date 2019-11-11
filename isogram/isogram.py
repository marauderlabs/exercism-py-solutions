from typing import Set

def is_isogram(string: str) -> bool:

    seen : Set(str) = set()
    for c in string:
        if not c.isalpha():
            continue

        l = c.lower()
        if l in seen:
            return False
        else:
            seen.add(l)

    return True
