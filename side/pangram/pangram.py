def is_pangram(sentence: str) -> bool:
    '''Returns true for a pangram'''
    # mark all chars as not seen
    # and strike them off as we see them.
    # When all are seen, it's a pangram.
    sentence = sentence.lower()
    not_seen = (1<<26)-1
    for c in sentence:
        if c.isalpha():
            not_seen &= ~(1 << (ord(c) - ord('a')))
        if not_seen == 0:
            return True
    return not_seen == 0
