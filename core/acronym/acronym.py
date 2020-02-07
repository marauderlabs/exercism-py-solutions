import string

def abbreviate(words: str) -> str:
    words = words.replace('-', ' ').upper()
    return "".join([w.lstrip(string.punctuation)[0] for w in words.split()])
