def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands aren't of equal length")

    dist = 0
    for a, b in zip(strand_a, strand_b):
        dist += int(a != b)
    return dist
