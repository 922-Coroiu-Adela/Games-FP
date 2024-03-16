class CustomDate:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month

    def __lt__(self, other):
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def to_string(self):
        return str(self.day) + "." + str(self.month)

