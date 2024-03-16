from Domain.Year import Year

class Repository:
    def __init__(self):
        self._current_year = Year()
        self._next_year = Year()

    def get_current_year(self):
        return self._current_year

    def set_current_year(self, current_year):
        self._current_year = current_year

    def get_next_year(self):
        return self._next_year

    def set_next_year(self, next_year):
        self._next_year = next_year

    def advance_year(self):
        self._next_year.set_year(self._current_year.get_year() + 1)
        self._current_year = self._next_year
        self._next_year = Year()



