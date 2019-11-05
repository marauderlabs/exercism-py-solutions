from typing import List

def latest(scores: List) -> int:
    if not scores:
        raise Exception("No scores")

    return scores[-1]


def personal_best(scores: List) -> int:
    if not scores:
        raise Exception("No scores")

    return sorted(scores, reverse=True)[0]


def personal_top_three(scores: List) -> List[int]:
    if not scores:
        raise Exception("No scores")

    return sorted(scores, reverse=True)[:3]
