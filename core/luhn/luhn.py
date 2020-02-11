class Luhn:
    def __init__(self, card_num: str):
        self.number: str = card_num
        self._valid = self.is_valid()

    def valid(self):
        return self._valid

    def strip_spaces(self) -> bool:
        '''Returns False if non-digit or non-whitespace chars are seen
        while stripping spaces off the string'''
        number = ""
        for n in self.number:
            if n.isspace():
                continue
            if not n.isdigit():
                return False
            number += n
        self.number = number
        return True

    def is_valid(self) -> bool:
        '''Returns True if it's valid Luhn number'''

        def double_odd(i: int, n: int) -> int:
            '''Return double n if i is odd'''
            if i % 2 != 0:
                return n*2 if n*2 < 10 else (n*2)-9
            return n

        if not self.strip_spaces():
            return False
        if len(self.number) < 2:
            return False
        number = [double_odd(i, int(n)) for i, n in enumerate(
                self.number[::-1])]
        return (sum(number) % 10 == 0)
