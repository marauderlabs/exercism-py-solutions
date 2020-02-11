MINS_IN_HOUR = 60
HOURS_IN_DAY = 24
MINS_IN_DAY = MINS_IN_HOUR*HOURS_IN_DAY


class Clock:
    def __init__(self, hour: int, minute: int):
        mins = (hour*MINS_IN_HOUR + minute) % MINS_IN_DAY
        if mins < 0:
            mins += MINS_IN_DAY
        self.mins: int = mins

    def __repr__(self) -> str:
        return '{:02d}:{:02d}'.format(
                self.mins//MINS_IN_HOUR, self.mins % MINS_IN_HOUR)

    def __eq__(self, other: 'Clock') -> bool:
        return self.mins == other.mins

    def __add__(self, minutes: int) -> 'Clock':
        return Clock(0, self.mins + minutes)

    def __sub__(self, minutes: int) -> 'Clock':
        return Clock(0, self.mins - minutes)
