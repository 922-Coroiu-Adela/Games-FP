import os

import Service.Service as Service
from prettytable import PrettyTable, ALL
import time


class UI:
    def __init__(self):
        self.service = Service.Service()

    def print_board(self):
        table = PrettyTable()
        board = self.service.get_board()
        new_board = []
        for row in board:
            new_row = []
            for cell in row:
                if cell == 0:
                    new_row.append(" ")
                else:
                    new_row.append("X")
            new_board.append(new_row)
        table.add_rows(new_board)
        table.header = False
        table.hrules = ALL
        print(table)

    def process_input(self, input):
        input = input.split(" ")
        if input[0] == "place" and len(input) == 4:
            try:
                self.place_pattern(input[1], int(input[2]), int(input[3]))
            except ValueError as ve:
                print(ve)
        elif input[0] == "tick" and len(input) == 2:
            try:
                self.service.tick(int(input[1]))
            except ValueError as ve:
                print(ve)
        elif input[0] == "exit" and len(input) == 1:
            exit(0)
        elif input[0] == "save" and len(input) == 2:
            self.service.save_to_filename(input[1])
        elif input[0] == "load" and len(input) == 2:
            self.service.load_from_filename(input[1])
        else:
            print("Invalid command!")

    def place_pattern(self, pattern_name, x, y):
        try:
            self.service.place_pattern(pattern_name, x, y)
        except ValueError as ve:
            print(ve)

    def run(self):
        while True:
            self.print_board()
            command = input("Enter command: ")
            self.process_input(command)