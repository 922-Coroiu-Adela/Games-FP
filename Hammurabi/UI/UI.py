from Service.Service import Service

class UI:
    def __init__(self):
        self.service = Service()

    def print_current_year(self):
        print(self.service.get_current_year().to_string())

    def print_actions_menu(self):
        while True:
            self.print_current_year()
            self.service.check_if_game_over()
            while True:
                try:
                    acres = int(input("Acres to buy/sell (+/-) -> "))
                    self.service.buy_sell_land(acres)
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    units = int(input("Grain to feed the population -> "))
                    self.service.feed_the_population(units)
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    planted_acres = int(input("Acres to plant -> "))
                    self.service.plant_acres(planted_acres)
                    break
                except ValueError as ve:
                    print(ve)
