class Gameboard:
    def __init__(self):
        self._board = [[0 for i in range(8)] for j in range(8)]
        self._patterns = {}
        self.read_patterns()

    def read_patterns(self):
        with open("patterns.txt") as file:
            for line in file:
                values = line.split(" ")
                pattern_name = values[0]
                pattern_coords = []
                for coords in values[1:]:
                    x, y = coords.split(",")
                    pattern_coords.append((int(x), int(y)))
                self._patterns[pattern_name] = pattern_coords

    def get_patterns(self):
        return self._patterns

    def get_board(self):
        return self._board

    def set_dead_cell(self, x, y):
        self._board[x][y] = 0

    def set_alive_cell(self, x, y):
        self._board[x][y] = 1