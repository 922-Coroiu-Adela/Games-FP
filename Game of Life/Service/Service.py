import Domain.Gameboard as Gameboard

class Service:
    def __init__(self):
        self.gameboard = Gameboard.Gameboard()
        self.future_gameboard = Gameboard.Gameboard()

    def get_board(self):
        return self.gameboard.get_board()

    def place_pattern(self, pattern_name, x, y):
        pattern_coords = self.gameboard.get_patterns()[pattern_name]
        for coords in pattern_coords:
            if x + coords[0] < 0 or x + coords[0] > 7 or y + coords[1] < 0 or y + coords[1] > 7:
                raise ValueError("Pattern cannot be placed outside of the board!")
            if self.gameboard.get_board()[x + coords[0]][y + coords[1]] == 1:
                raise ValueError("Pattern cannot be placed on live cell!")
        for coords in pattern_coords:
            self.gameboard.set_alive_cell(x + coords[0], y + coords[1])

    def compute_next_generation(self):
        '''
        Computes the next generation of the gameboard following the rules of the game
        :return:
        '''
        for i in range(8):
            for j in range(8):
                # count number of live neighbors
                live_neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if i + x < 0 or i + x > 7 or j + y < 0 or j + y > 7:
                            continue
                        if self.gameboard.get_board()[i + x][j + y] == 1:
                            live_neighbors += 1
                # apply rules
                if self.gameboard.get_board()[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        self.future_gameboard.set_dead_cell(i, j)
                    else:
                        self.future_gameboard.set_alive_cell(i, j)
                else:
                    if live_neighbors == 3:
                        self.future_gameboard.set_alive_cell(i, j)
        self.gameboard = self.future_gameboard
        self.future_gameboard = Gameboard.Gameboard()

    def tick(self, n):
        '''
        Computes the next n generations
        :param n: number of generations
        :return:
        '''
        for i in range(n):
            self.compute_next_generation()

    def save_to_filename(self, filename):
        with open(filename, "w+") as file:
            board = self.gameboard.get_board()
            for i in range(8):
                for j in range(8):
                    file.write(str(self.gameboard.get_board()[i][j]) + ",")
                file.write("\n")

    def load_from_filename(self, filename):
        board = []
        with open(filename, "r") as file:
            for line in file:
                values = line.split(",")
                row = []
                for i in range(8):
                    row.append(int(values[i]))
                board.append(row)
        print(board)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    self.future_gameboard.set_alive_cell(i, j)
                else:
                    self.future_gameboard.set_dead_cell(i, j)
        self.gameboard = self.future_gameboard
        self.future_gameboard = Gameboard.Gameboard()