from Controller.Control_Class import Controller


class UI:
    def __init__(self):
        self.controller = Controller()

    def process_command(self, command):
        params = command.split()
        return params

    def start_app(self):
        lst = self.controller.controller_get_sentence()
        print(lst[1], "[score is: ", lst[0], "]")
        self.controller.controller_scramble_letters()
        while True:
            lst = self.controller.controller_get_sentence()
            print(lst[1], "[score is: ", lst[0], "]")
            try:
                command = input()
                command = self.process_command(command)

                if command[0] == 'swap':
                    self.controller.controller_swap_letters(int(command[1]), int(command[2]), int(command[4]), int(command[5]))
                    self.controller.controller_update_score()
                    if self.controller.controller_check_win() == True:
                        print("You won!")
                        exit()
                    if self.controller.controller_check_lose() == True:
                        print("You lost!")
                        exit()
            except Exception:
                print("Invalid input!")
